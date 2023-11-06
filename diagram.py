from diagrams import Diagram,Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
#from diagrams.onprem.client import Client
from diagrams.programming.framework import *
from diagrams.programming.language import *
from diagrams.generic.database import *
from diagrams.onprem.client import Users
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.database import *
from diagrams.onprem.ci import Jenkins

with Diagram("IS 436 ", show=False, direction="TB"):
    client=Users("client")
    Angular("Angular") >> Java("java") >> Spring("Spring")
   

    with Cluster("Group component"):
        workers=Jenkins("Jenkins") 
    with Cluster("Group Cluster"):
        source= PHP("Backend") >> SQL("DB") >> PostgreSQL("PGaDmin")

    client << source
    client >> source