import pandas as pd

# Load the TSV file
df = pd.read_csv("../reflection-tree.tsv", sep="\t")

# Convert rows into dictionary for fast access
nodes = {row['id']: row for _, row in df.iterrows()}

current = "START"
answers = {}

print("=== Daily Reflection Agent ===")

while True:
    node = nodes[current]

    # Show text
    if pd.notna(node['text']):
        print("\n" + str(node['text']))

    # END NODE
    if node['type'] == "end":
        print("\nSession completed. Thank you!")
        break

    # QUESTION NODE
    elif node['type'] == "question":
        options = str(node['options']).split("|")

        # Show options
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        # Get input safely
        while True:
            try:
                choice = int(input("Select option: ")) - 1
                if 0 <= choice < len(options):
                    break
                else:
                    print("Invalid choice. Try again.")
            except:
                print("Enter a valid number.")

        selected = options[choice]
        answers[current] = selected

        # Move to next child
        next_nodes = df[df['parentId'] == current]

        if not next_nodes.empty:
            current = next_nodes.iloc[0]['id']
        else:
            print("No next node found.")
            break

    # DECISION NODE
    elif node['type'] == "decision":
        rules = str(node['options']).split(";")

        prev_answer = list(answers.values())[-1]

        matched = False

        for rule in rules:
            condition, target = rule.split(":")
            values = condition.split("=")[1].split("|")

            if prev_answer in values:
                current = target
                matched = True
                break

        if not matched:
            print("No matching decision rule found.")
            break

    # OTHER NODES (start, reflection, bridge, summary)
    else:
        next_nodes = df[df['parentId'] == current]

        if not next_nodes.empty:
            current = next_nodes.iloc[0]['id']
        else:
            break


### How to run 
cd agent 
python main.py
