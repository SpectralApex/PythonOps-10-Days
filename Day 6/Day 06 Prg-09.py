# Mind Map Generator
def generate_mind_map(topic, branches):
    print(f"\n🧠 Mind Map: {topic}")
    for i, branch in enumerate(branches, 1):
        print(f"  {i}. {branch}")
        subtopics = input(f"    → Subtopics for '{branch}': ").split(",")
        for sub in subtopics:
            print(f"      - {sub.strip()}")

generate_mind_map("Cybersecurity", ["Network Security", "Threat Analysis", "Ethical Hacking"])
