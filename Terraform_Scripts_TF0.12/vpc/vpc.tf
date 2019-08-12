# Create a new VPC
resource "aviatrix_vpc" "test_vpc" {
  account_name          = "AWSAccess"
  aviatrix_transit_vpc  = false
  aviatrix_firenet_vpc  = false
  cidr                  = "11.11.11.11/24"
  cloud_type            = 1
  name                  = "createVPCTest"
  region                = "us-west-1"
}

resource "aviatrix_vpc" "test_vpc2" {
  account_name          = "AWSAccess"
  aviatrix_transit_vpc  = true
  aviatrix_firenet_vpc  = false
  cidr                  = "10.10.10.10/20"
  cloud_type            = 1
  name                  = "createVPCTest2"
  region                = "us-east-1"
}

resource "aviatrix_vpc" "test_vpc3" {
  account_name          = "AWSAccess"
  aviatrix_transit_vpc  = false
  aviatrix_firenet_vpc  = true
  cidr                  = "13.13.13.13/24"
  cloud_type            = 1
  name                  = "createVPCTest3"
  region                = "us-west-2"
}
