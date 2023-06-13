with open("Input/Names/invited_names.txt", mode="r") as names:
    for x in names:
        name = x.strip()
        with open("Input/Letters/starting_letter.txt") as draft:
            with open(f"Output/ReadyToSend/{name}_invite.txt", mode="a") as letter:
                draft_content = draft.read()
                updated_content = draft_content.replace("[name]", name) + "\n"
                letter.write(updated_content)


