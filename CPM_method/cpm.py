import json
import networkx as nx
import matplotlib.pyplot as plt


def cpm(activities):
    early_start_times = {}
    early_finish_times = {}
    late_start_times = {}
    late_finish_times = {}
    total_slacks = {}

    # Calculate the early start and finish times for each activity
    for activity in activities:
        if activity.predecessors == []:
            early_start_times[activity.id] = 0
            early_finish_times[activity.id] = activity.duration
        else:
            early_start_times[activity.id] = max(
                [early_finish_times[predecessor_id] for predecessor_id in activity.predecessors])
            early_finish_times[activity.id] = early_start_times[activity.id] + \
                activity.duration

    # Calculate the project duration
    project_duration = max([early_finish_times[activity.id]
                           for activity in activities])

    # Calculate the late start and finish times for each activity
    for activity in reversed(activities):
        if activity.successors == []:
            late_finish_times[activity.id] = project_duration
            late_start_times[activity.id] = late_finish_times[activity.id] - \
                activity.duration
        else:
            late_finish_times[activity.id] = min(
                [late_start_times[successor_id] for successor_id in activity.successors])
            late_start_times[activity.id] = late_finish_times[activity.id] - \
                activity.duration

    # Calculate the total slack for each activity
    for activity in activities:
        total_slacks[activity.id] = late_start_times[activity.id] - \
            early_start_times[activity.id]

    # Identify the critical path
    critical_path = []
    for activity in activities:
        if total_slacks[activity.id] == 0:
            critical_path.append(activity.name)

    print("Activity Details:")
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Activity",
          "Duration", "Early Start", "Early Finish", "Late Start", "Late Finish", "Slack Time"))

    for activity in activities:
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            activity.name,
            activity.duration,
            early_start_times[activity.id],
            early_finish_times[activity.id],
            late_start_times[activity.id],
            late_finish_times[activity.id],
            total_slacks[activity.id]
        ))

    return critical_path


# Define an activity class
class Activity:
    def __init__(self, id, name, duration, predecessors):
        self.id = id
        self.name = name
        self.duration = duration
        self.predecessors = predecessors
        self.successors = []

    def __str__(self):
        return f"Activity(id={self.id}, duration={self.duration}, predecessors={self.predecessors}, successors={self.successors})"

    def add_successor(self, successor):
        self.successors.append(successor)


# Load the JSON file
with open('./CPM_method/input.json') as f:
    data = json.load(f)

# Create activities from the JSON data
activities = []
for activity_data in data['activities']:
    activity = Activity(activity_data['id'], activity_data['name'],
                        activity_data['duration'], activity_data['predecessors'])
    activities.append(activity)

# Add successors to each activity
for activity1 in activities:
    for predecessor_id in activity1.predecessors:
        for activity2 in activities:
            if activity2.id == predecessor_id:
                activity2.add_successor(activity1.id)


# [print(activitie) for activitie in activities]

# Calculate the critical path
critical_path = cpm(activities)

# Print the critical path
print(f"\n{critical_path}")


nodes = []
edges = []
for activity in activities:
    nodes.append(activity.name)
    for predecessor_id in activity.predecessors:
        edges.append((activity.name, activities[predecessor_id].name))


def node_color(node):
    for activity in critical_path:
        if activity == node:
            return 'red'
    return 'blue'


network_graph = nx.Graph()
network_graph.add_nodes_from(nodes)
network_graph.add_edges_from(edges)
node_colors = [node_color(node) for node in network_graph.nodes()]
nx.draw(network_graph, with_labels=True,
        node_color=node_colors, node_size=1000)

plt.show()
