from ..file_manager import open_json
from ..Request import Request


def view_request():
    requests = open_json("requests.json", "read")

    if not requests:
        print("\nNo requests found.\n")
        return

    # Table header
    print(f"{'ID':<12}{'Description':<25}{'Client':<20}{'Project':<20}{'Timestamp':<25}")
    print("-" * 102)

    # Table rows
    for r in requests:
        print(f"{r['id']:<12}{r['description']:<25}{r['client']:<20}{r['project']:<20}{r['timestamp']:<25}")

    print("\n")  # extra spacing


def add_request():
    print("Add the new request data:")

    # Simple loop until valid input is entered
    while True:
        description = input("Enter description: ").strip()
        if not description or (len(description)>5000 or len(description)<10):
            print("Description cannot be empty!")
        else :
             break
    while True:
        client = input("Enter client info: ").strip()
        if client:
            break
        print("Client cannot be empty!")

    while True:
        project = input("Enter project info: ").strip()
        if project:
            break
        print("Project cannot be empty!")

    # Create Request object
    request = Request(description=description, client=client, project=project).__dict__

    # Append to JSON file
    open_json("requests.json", "append", request)

    print("\n✅ Request added successfully!\n")




def update_request():
    # Load existing requests
    requests = open_json("requests.json", "read")

    if not requests:
        print("No requests to update.")
        return

    # Show all requests with their IDs
    print(f"{'ID':<12}{'Description':<25}{'Client':<20}{'Project':<20}{'Timestamp':<25}")
    print("-" * 102)
    for r in requests:
        print(f"{r['id']:<12}{r['description']:<25}{r['client']:<20}{r['project']:<20}{r['timestamp']:<25}")

    # Ask user which ID to update
    update_id = input("Enter the ID of the request to update: ").strip()

    # Find the request
    request_to_update = None
    for r in requests:
        if str(r['id']) == update_id:
            request_to_update = r
            break

    if not request_to_update:
        print(f"No request found with ID {update_id}.")
        return

    # Update fields (press Enter to keep existing value)
    new_description = input(f"Enter new description [{request_to_update['description']}]: ").strip()
    if new_description:
        request_to_update['description'] = new_description

    new_client = input(f"Enter new client [{request_to_update['client']}]: ").strip()
    if new_client:
        request_to_update['client'] = new_client

    new_project = input(f"Enter new project [{request_to_update['project']}]: ").strip()
    if new_project:
        request_to_update['project'] = new_project

    # Save back updated requests
    open_json("requests.json", "write", requests)
    print(f"✅ Request with ID {update_id} updated successfully!")

def delete_request():
    # Load existing requests
    requests = open_json("requests.json", "read")

    if not requests:
        print("No requests to delete.")
        return

    # Show all requests with their IDs
    print(f"{'ID':<12}{'Description':<25}{'Client':<20}{'Project':<20}{'Timestamp':<25}")
    print("-" * 102)
    for r in requests:
        print(f"{r['id']:<12}{r['description']:<25}{r['client']:<20}{r['project']:<20}{r['timestamp']:<25}")

    # Ask user which ID to delete
    delete_id = input("Enter the ID of the request to delete: ").strip()

    # Check if the ID exists
    new_requests = [r for r in requests if str(r['id']) != delete_id]

    if len(new_requests) == len(requests):
        print(f"No request found with ID {delete_id}.")
        return

    # Save the updated list back
    open_json("requests.json", "write", new_requests)
    print(f"✅ Request with ID {delete_id} deleted successfully!")
