import csv

#Insert some code here
class DataHandler:
    def __init__(self, filename="festival_goers.csv"):
        """Initialize with a CSV filename and load data."""
        self.filename = filename
        #There's something fishy here 
        self.filename = filename 
        self.data = self.load_from_csv() 

        original_count = len(self.data)

        self.data = self.remove_duplicates(self.data)

        if len(self.data) < original_count:
            self.save_to_csv()

        self.gigs = {
            "Day 1": ["Fink Ployd", "Psychedelic corn trumpets"],
            "Day 2": ["Porcupine Bush", "Fever Day"],
            "Day 3": ["Pearl Djam", "Soundbackyard"]
        }

    def remove_duplicates(self, data):
        """Remove exact duplicate rows while preserving order."""
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

    def is_duplicate(self, name, age, distance, accommodation, ticket_type):
        """Check whether the same festival-goer already exists."""

        new_record = (
            name.strip().lower(),
            int(age),
            float(distance),
            accommodation.strip().lower(),
            ticket_type.strip().lower()
        )

        for person in self.data:
            try:
                existing_record = (
                    str(person.get("Name", "")).strip().lower(),
                    int(person.get("Age")),
                    float(person.get("Distance")),
                    str(person.get("Accommodation", "")).strip().lower(),
                    str(person.get("Ticket", "")).strip().lower()
                )
            except (ValueError, TypeError):
                continue

            if new_record == existing_record:
                return True

        return False

    def load_from_csv(self):
        """Load festival-goers from the CSV file."""
        try:
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                return [row for row in reader]  # Load all rows as dictionaries
        except FileNotFoundError:
            return []

    def save_to_csv(self):
        """Save the current festival-goer data back to the CSV file."""
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ["Name", "Age", "Distance", "Accommodation", "Ticket"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def add_festival_goer(self, name, age, distance, accommodation, ticket_type):
        """Add a new festival-goer and save to CSV."""

        if self.is_duplicate(name, age, distance, accommodation, ticket_type):
            return False

        person = {
            "Name": name,
            "Age": int(age),
            "Distance": float(distance),
            "Accommodation": accommodation,
            "Ticket": ticket_type
        }

        self.data.append(person)
        self.save_to_csv()

        return True

    def filter_by_ticket(self, ticket_type):
        """Return a list of people with a specific ticket type."""
        return [person for person in self.data if person["Ticket"] == ticket_type]

    def get_distribution_by_accommodation(self, ticket_type):
        """Get the distribution of accommodations for a specific ticket type."""
        filtered = self.filter_by_ticket(ticket_type)
        distribution = {}
        for person in filtered:
            accommodation = person["Accommodation"]
            distribution[accommodation] = distribution.get(accommodation, 0) + 1
        return distribution

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

            return [ 
                person for person in self.data 
                if person["Ticket"] == "Full Access" 
            ] 

        return [] 