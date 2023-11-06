from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
#from diagrams.onprem.client import Client
from diagrams.programming.framework import *
from diagrams.programming.language import *
from diagrams.generic.database import *


with Diagram("Grouped Workers", show=False, direction="TB"):
 
    Angular("Angular") >> Java("java") >>Spring("Spring")
    PHP("Backend") >> SQL("DB")