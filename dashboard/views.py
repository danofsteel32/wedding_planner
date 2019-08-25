import hashlib
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
)
from django.db import IntegrityError
from django.http import Http404
from .models import Guest, Party


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':

        # Load everything into RAM
        invitations = Party.objects.all()
        guests = Guest.objects.all()

        # calc stats
        total_invitations = invitations.count()
        sent_invitations = invitations.filter(sent=True).count()
        total_guests = guests.count() + sum([g.plus_ones for g in guests])
        guests_rsvp = guests.filter(rsvp=True).all()
        total_rsvp = guests_rsvp.count() + sum([g.plus_ones for g in guests_rsvp])

        context = dict(
            total_invitations=total_invitations,
            sent_invitations=sent_invitations,
            total_guests=total_guests,
            total_rsvp=total_rsvp,
            party_list=invitations,
        )
        return render(request, 'dashboard/index.html', context)


def details(request, party_id):
    # return guests associated with Party id
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        print(party_id)
        party = get_object_or_404(Party, pk=party_id)
        party_guests = get_list_or_404(Guest, party=party_id)

        guests = list()
        for g in party_guests:
            name = g.first_name.title() + ' ' + g.last_name.title()
            guests.append(dict(
                id=g.id,
                name=name,
                plus_ones=g.plus_ones,
                rsvp=g.rsvp,
            ))

        context = dict(party=party, guests=guests)

        return render(request, 'dashboard/details.html', context)


def addnew(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        return render(request, 'dashboard/addnew.html')


def edit(request, party_id):

    if request.method == 'POST':
        print(party_id)
        p = request.POST
        print(p)

        Party.objects.filter(pk=party_id).update(
            description=p['description'],
            street=p['street'],
            city=p['city'],
            state=p['state'],
            zip_code=p['zip_code'],
            phone_number=p['phone_number'],
            # p['sent'] will only exist if rsvp button was clicked at form
            sent=True if 'sent' in p else False,
        )

        # p.getlist('guest_id') = ['1', '2', ...] corresponding to number of guests
        idx = 0
        for n in p.getlist('guest_id'):
            name = p.getlist('name')[idx].split()

            if len(name) == 1:
                last_name = ''
            else:
                last_name = name[1]

            Guest.objects.filter(pk=int(n)).update(
                first_name=name[0],
                last_name=last_name,
                plus_ones=p.getlist('plus_ones')[idx],
                # p['rsvp<n>'] will only exist if rsvp button was clicked at form
                rsvp=True if 'rsvp' + n in p else False,
            )
            idx += 1

        return redirect('dashboard:index')


def add(request):

    if request.method == 'POST':
        p = request.POST
        print(p)

        m = hashlib.sha1()
        hash_str = p['description'] + p['street'] + p['city'] + p['state'] + p['zip_code']
        m.update(hash_str.encode('utf-8'))

        try:
            party = Party(
                description=p['description'],
                street=p['street'],
                city=p['city'],
                state=p['state'],
                zip_code=p['zip_code'],
                phone_number=p['phone_number'],
                rsvp_id=m.hexdigest(),
            )
            party.save()

        except IntegrityError:
            raise Http404('That party already exists')

        for n in p.getlist('name'):
            name = n.split()

            if len(name) == 1:
                last_name = ''
            else:
                last_name = name[1]

            guest = Guest(
                party=party,
                first_name=name[0],
                last_name=last_name,
            )
            guest.save()

        return redirect('dashboard:index')
