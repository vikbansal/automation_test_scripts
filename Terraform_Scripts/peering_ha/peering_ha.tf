# Enter your controller's IP, username and password to login
provider "aviatrix" {
  controller_ip = "${var.aviatrix_controller_ip}"
       username = "${var.aviatrix_controller_username}"
       password = "${var.aviatrix_controller_password}"
}
resource "aviatrix_gateway" "GW" {
          count = "${length(var.aws_vpc_id)}"
     cloud_type = "${var.aviatrix_cloud_type_aws}"
   account_name = "${var.aviatrix_cloud_account_name}"
        gw_name = "${element(var.gateway_names,count.index)}"
         vpc_id = "${element(var.aws_vpc_id,count.index)}"
        vpc_reg = "${var.aws_region}"
       vpc_size = "${var.aws_instance}"
        vpc_net = "${element(var.aws_vpc_public_cidr,count.index)}"
  public_subnet = "${element(var.aws_vpc_public_cidr,count.index)}"
}

# Create encrypteed peering between two aviatrix gateway
resource "aviatrix_tunnel" "PEERING"{
           vpc_name1 = "${var.gateway_names[0]}"
           vpc_name2 = "${var.gateway_names[1]}"
           enable_ha = "${var.enable_ha}"
             cluster = "no"
    over_aws_peering = "no"
    peering_hastatus = "yes"
          depends_on = ["aviatrix_gateway.GW"]
}
