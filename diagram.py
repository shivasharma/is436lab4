from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
#from diagrams.onprem.client import Client
from diagrams.programming.framework import *
from diagrams.programming.language import *
from diagrams.generic.database import *
from diagrams.onprem.client import Users
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.ci import Jenkins
with Diagram("IS 436 ", show=False, direction="TB"):
    Users("client")
    Angular("Angular") >> Java("java") >> Spring("Spring")
    PHP("Backend") >> SQL("DB") >> PostgreSQL("PGaDmin")
    Jenkins("Ci/CD")