# Write a script to validate voter eligibility in nigeria

# criteria to vote during election
age = 18
citizenship = 'yes'
registration = 'yes'
sanity = 'yes'
residency = 'lagos'
legal_status = 'no'

# checking voters qualification
voter_age = int(input('How old are you? >>> '))

voter_citizenship = input('Are you a citizen of nigeria (yes/no) >>> ').strip().lower()

voter_registration = input('Are you a registered voter (yes/no) >>> ').strip().lower()

voter_sanity = input('Are you of sound mind (yes/no) >>> ').strip().lower()

voter_residency = input('Where do you leave (lagos/elsewhere) >>> ').strip().lower()

voter_legal_status = input('Have you ever been arrested or have a problem with the law (yes/no) >>> ').strip().lower()

# qualifying or disqualifying voters based on input
if voter_age >= 18:
    if voter_citizenship == citizenship:
        if voter_registration == registration:
            if voter_sanity == sanity:
                if voter_residency == residency:
                    if voter_legal_status == legal_status:
                        print('YOU CAN CAST YOUR VOTE!')
                    else:
                        print('Disqualified (Reason): legal_status issue')
                else:
                    print('Disqualified (Reason): Residency issue')    
            else:
                print('Disqualified (Reason): Sanity issue')
        else:
            print('Disqualified (Reason): Registration issue')   
    else:
        print('Disqualified (Reason): Citizenship issue')
else:
    print('Disqualified (Reason): Age issue')                                 

