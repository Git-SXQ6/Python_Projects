import csv
import os

class DataHandler:
    def __init__(self, filename="festival_goers.csv"):
        # Bug 9: Make sure festival_goers.csv can be opened
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, filename) 
        self.data = self.load_from_csv() # this was commented out, meaning that the CSV is not loaded on start up
        
        # Bug 10: Remove duplicate data from festival_goers.csv file in program
        # and update it in the csv file
        original_count = len(self.data)
        self.data = self.remove_duplicates(self.data)

        if len(self.data) < original_count:
            self.save_to_csv()

        self.gigs = {
            "Day 1": ["Fink Ployd", "Psychedelic corn trumpets"],
            "Day 2": ["Porcupine Bush", "Fever Day"],
            "Day 3": ["Pearl Djam", "Soundbackyard"]
        }

    def load_from_csv(self):
        """Load festival-goers from the CSV file."""
        try:
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                # Bug 4 - not sure if it would be useful for visualization? - can reassess later
                #return [row for row in reader]  # Load all rows as dictionaries
                data = []

                for row in reader:
                    try:
                        row["Age"] = int(row["Age"])
                    except (ValueError, TypeError, KeyError):
                        row["Age"] = None

                    try:
                        row["Distance"] = float(row["Distance"])
                    except (ValueError, TypeError, KeyError):
                        row["Distance"] = None
                    
                    data.append(row)

                return data

        # Unsure what to keep yet, leave here for further discussion
        except FileNotFoundError:
            print("CSV file not found.")
            return []

        except Exception as e:
            print("Unexpected error:", repr(e))
            raise
        
    def remove_duplicates(self, data):
    #Bug 10: """Remove duplicate rows."""
        unique_data = []
        seen = set()

        for person in data:
            record = (
                person.get("Name"),
                person.get("Age"),
                person.get("Distance"),
                person.get("Accommodation"),
                person.get("Ticket")
            )

            if record not in seen:
                seen.add(record)
                unique_data.append(person)

        return unique_data

# BUG (): prevent duplicate for festival goer input
    def is_duplicate(self, name, age, distance, accommodation, ticket_type):
        """Check whether the same festival-goer already exists."""

        try:
            age = int(age)
            distance = float(distance)
        except ValueError:
            return False

        new_record = (
            name.strip().lower(),
            age,
            distance,
            accommodation.strip().lower(),
            ticket_type.strip().lower()
        )

        for person in self.data:
            existing_record = (
                str(person.get("Name", "")).strip().lower(),
                person.get("Age"),
                person.get("Distance"),
                str(person.get("Accommodation", "")).strip().lower(),
                str(person.get("Ticket", "")).strip().lower()
            )

            if new_record == existing_record:
                return True

        return False

    def save_to_csv(self):
        """Save the current festival-goer data back to the CSV file."""
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ["Name", "Age", "Distance", "Accommodation", "Ticket"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

# check data type
    def add_festival_goer(self, name, age, distance, accommodation, ticket_type):
        """Add a new festival-goer and save to CSV."""
        person = {
            "Name": name,
            "Age": int(age),
            "Distance": float(distance),
            "Accommodation": accommodation,
            "Ticket": ticket_type
        }

        self.data.append(person)
        self.save_to_csv()

    def filter_by_ticket(self, ticket_type):
        """Return a list of people with a specific ticket type."""
        # Bug 2: return a list of people with specific ticket type
        return [person for person in self.data if person["Ticket"] == ticket_type]
    # The code here was: return [person for person in self.data if person["Ticket"] != ticket_type] 
    # The != is supposed to be ==
    # The method is supposed to return peope with that ticket type but the condition 
    # "!=" returns everyone except that type

    def get_distribution_by_accommodation(self, ticket_type):
        """Get the distribution of accommodations for a specific ticket type."""
        filtered = self.filter_by_ticket(ticket_type)
        distribution = {}
        for person in filtered:
            accommodation = person["Accommodation"]
            distribution[accommodation] = distribution.get(accommodation, 0) + 1
        return distribution

# ==========================================================================================#
# VERSION 1
# ==========================================================================================#

    # def get_eligible_festival_goers(self, day):
    #         """Get festival-goers eligible for gigs on a specific day."""
    #     if day == "Day 1":
    #         return self.data
    #         day_number = day.split()[1] # Day 2 -> 2 
    #         day_ticket = f"{day_number} Day" # Changes it from Day 2 to 2 Day 
    #     # This change is because the tickets are saved as 2 Day and not Day 2
    #     # The comparison never matched anyone except Full Access holders, and 
    #     # Anyone with a 1 Day or 2 Day ticket were invinsible when clicked on a gig
    #     # The fix is to just flip the format
    #     return [person for person in self.data if person["Ticket"] in ["Full Access", f"{day}"]]

# ==========================================================================================#
# VERSION 2
# ==========================================================================================#

# This function mixed up two concepts. 
# But we cannot get enough info from the ticket type of "1 day", "2 day"
# to know which dates they are eligible for, so I think there is a bigger
# issue with the way we collected information
    def get_eligible_festival_goers(self, day):
        """Get festival-goers eligible for gigs on a specific day."""
        if day == "Day 1":
            return [
                person for person in self.data
                if person["Ticket"] in ["1 Day", "2 Day", "Full Access"]
            ]
        elif day == "Day 2":
            return [
                person for person in self.data
                if person["Ticket"] in ["2 Day", "Full Access"]
            ]
        elif day == "Day 3":
            return[
                person for person in self.data
                if person["Ticket"] == "Full Access"
            ]
        return []