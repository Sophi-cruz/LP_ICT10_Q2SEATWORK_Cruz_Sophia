from pyscript import document 

def candidate_checker(e): 
    club_members = ["procyon lotor", "procyon cancrivorus", "procyon pygmaeus"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    if member_checker:
        message = f'Woahahah {candidate}, you are now part of the raccoon bins!'
    else:
        message = f'Sorry {candidate}, youre not on the list.'
 
    document.getElementById('result').innerHTML = message