## TGW-related
variable "security_domain_name_list" {
  type = list(string)
}
variable "connected_domains_list1" {
  type = list(string)
}
variable "connected_domains_list2" {
  type = list(string)
}
variable "connected_domains_list3" {
  type = list(string)
}
variable "connected_domains_list4" {
  type = list(string)
}

## attached_vpc parameters
variable "aws_vpc_id" {
  type = list(string)
}
variable "custom_routes_list" {}
variable "disable_local_route_propagation" {}