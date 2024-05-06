NUMBER_OF_MEMBERS = 5

individuals = {}  # ID: [name, points]
teams = {}  # ID: [team_name, [members], points]
events = {}  # ID: [is team event?, name, [participants]]

def output_data(data):
    print(f"{data}:")
    if data == "Individuals":
        for individual in individuals:
            print(f"ID: {individual}, Name: {individuals[individual][0]}")

    elif data == "Teams":
        for team in teams:
            print(f"ID: {team}, Name: {teams[team][0]}, Members: {str(teams[team][1]).strip('[]')}")

    elif data == "Events":
        for event in events:
            print(f"ID: {event}, Name: {events[event][1]}, Participants: {str(events[event][2]).strip('[]')}")


def enter_participant():
    choice = input("Do you want to enter a individual or team participant? Please enter '1' for individual or '2' for team:  ")
    if choice == "1":
        get_individual_participant()
    elif choice == "2":
        get_team_participants()
    else:
        print("Invalid participant type.")


def get_individual_participant():
    name = input("Please enter the name of the participant:  ")
    id = len(individuals) + 1
    individuals.update({str(id): [name, 0]})
    print(f"This participant will have the ID: {id}")


def get_team_participants():
    team_name = input("Please enter the name of the team:  ")
    team_members = []
    for _ in range(NUMBER_OF_MEMBERS):
        name = input("Please enter the name of the participant:  ")
        team_members.append(name)

    id = len(teams) + 1
    teams.update({str(id): [team_name, team_members, 0]})
    print(f"This team will have the ID: {id}")


def create_event():
    choice = input("Do you want to create an individual or team event? Please enter '1' for individual or '2' for team:  ")
    name = input("Please enter the name of the event:  ")
    id = len(events) + 1
    events.update({str(id): [False if choice == "1" else True, name, []]})  # ID: [is team event?, name, [List of participants]]
    print(f"This event will have the ID: {id}")


def add_participants():
    output_data("Events")
    event = input("Please enter the id of the event:  ")
    output_data('Teams' if events[event][0] else 'Individuals')
    participant_id = input(f"Please enter the id of the {'team' if events[event][0] else 'individual'}:  ")
    events[event][2].append(participant_id)


def enter_results():
    for event in events:
        if events[event][2] == []:  # If there are no participants in the event
            print(f"There are no participants in event {event}")
            continue

        for participant in events[event][2]:  # Gets the ID of each participant
            if not events[event][0]:  # Individual event
                output_data("Individuals")
                place = int(input(f"Please enter the place for participant {participant} in the {events[event][1]} event:  "))
                individuals[participant][1] += max(1, 5 - place)
            else:  # Team event
                output_data("Teams")
                place = input(f"Please enter the place for team {participant} in the {events[event][1]} event:  ")
                teams[participant][2] += max(1, 5 - int(place))


def display_results():  
    print("\n\nIndividuals")
    for individual in individuals:
        print(f"{individuals[individual][0]}: {individuals[individual][1]}")
    print("\nTeams")
    for team in teams:
        print(f"{teams[team][0]}: {teams[team][2]}")


def menu():
    while True:
        print(
            """
  Menu:
  1. Enter participants
  2. Enter events
  3. Add participants to events
  4. Run tournament
  5. Exit
  """
        )
        choice = input("Enter your choice:  ")
        if choice == "1":
            enter_participant()
            continue
        elif choice == "2":
            create_event()
            continue
        elif choice == "3":
            add_participants()
            continue
        elif choice == "4":
            enter_results()
            display_results()
            continue
        elif choice == "5":
            exit()
        else:
            print("Invalid choice")


menu()
