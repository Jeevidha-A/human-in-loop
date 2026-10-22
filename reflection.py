
def generate_email(reason, leave_date):
    subject = f"Leave Request - {leave_date}"

    # Initial email draft
    content = (
        f"I would like to request leave on {leave_date} "
        f"due to {reason}."
    )

    return subject, content


def check_email(content):
    # Check whether the email contains a polite request
    if "kindly approve my request" not in content.lower():
        return False

    # Check whether the email ends with a full stop
    if not content.endswith("."):
        return False

    return True


def correct_email(content):
    print("Checking email...")

    # Automatically fix missing polite wording
    if "kindly approve my request" not in content.lower():
        content = content.rstrip(". ") + (
            ". Kindly approve my request."
        )

    # Ensure the email ends with a full stop
    if not content.endswith("."):
        content += "."

    return content


def main():
    print("=== Self-Correction Agent ===")

    reason = input("Enter your leave reason: ").strip()
    leave_date = input("Enter your leave date: ").strip()

    if not reason or not leave_date:
        print("Error: Reason and date cannot be empty.")
        return

    # Step 1: Generate email
    subject, content = generate_email(reason, leave_date)

    print("\nInitial email:")
    print("Subject:", subject)
    print("Content:", content)

    # Step 2: Check the email
    if not check_email(content):
        print("\nIssue found in the email.")

        # Step 3: Correct the issue automatically
        content = correct_email(content)

    # Step 4: Check again
    if check_email(content):
        print("\nEmail passed the checks!")
    else:
        print("\nEmail still has an issue. Please review it.")
        return

    # Step 5: Display and save the final email
    print("\n--- Final Email ---")
    print("Subject:", subject)
    print("Content:", content)

    with open("final_email.txt", "w") as file:
        file.write(f"Subject: {subject}\n\n")
        file.write(f"Content: {content}\n")

    print("\nFinal email saved to final_email.txt")


if __name__ == "__main__":
    main()
