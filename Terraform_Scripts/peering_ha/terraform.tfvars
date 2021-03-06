
aviatrix_cloud_type_aws = "1"
aviatrix_cloud_account_name  = "PrimaryAccessAccount"
gateway_names       = ["peeringHA-gw1","peeringHA-gw2"]
aws_region          = "us-east-1"
aws_instance        = "t2.micro"
aws_vpc_id          = ["vpc-abc123","vpc-def456"]
aws_vpc_public_cidr = ["10.0.0.0/24","11.0.0.0/24"]
avx_peering_eip     = ["11.11.11.11", "12.12.12.12"]

enable_ha           = "yes"
# enable_cluster      = "no"
