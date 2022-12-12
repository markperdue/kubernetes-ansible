from diagrams import Cluster, Diagram
from diagrams.k8s.infra import Master, Node
from diagrams.onprem.iac import Ansible

no_margin = {
    "margin": "-2"
}

margin = {
    "margin": "8"
}

with Diagram("", filename="kubernetes-cluster", graph_attr=no_margin, show=False, direction="TB"):
    with Cluster("Control Plane Nodes", graph_attr=margin):
        control_planes = Master("c1-cp1.lab")
    with Cluster("Worker Nodes", graph_attr=margin):
        workers = [
            Node("c1-node3.lab"),
            Node("c1-node2.lab"),
            Node("c1-node1.lab"),
        ]

    ansible = Ansible()

    ansible >> control_planes
    ansible >> workers
