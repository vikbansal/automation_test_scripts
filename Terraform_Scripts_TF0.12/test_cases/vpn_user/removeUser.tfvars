# Test order 5: revert all previous changes, remove user

aviatrix_vpn_profile_user_list  = ["testdummy1"]

aviatrix_vpn_profile_action     = ["allow", "deny"]
aviatrix_vpn_profile_protocol   = ["all",
                                   "tcp",
                                   "udp",
                                   "icmp",
                                   "sctp",
                                   "rdp",
                                   "dccp"]

aviatrix_vpn_profile_port       = ["0:65535",
                                   "5555",
                                   "5566",
                                   "0:65535",
                                   "5588",
                                   "5599",
                                   "5600"]

aviatrix_vpn_profile_target     = ["10.0.0.0/32",
                                   "11.0.0.0/32",
                                   "12.0.0.0/32",
                                   "13.0.0.0/32",
                                   "14.0.0.0/32",
                                   "15.0.0.0/32",
                                   "16.0.0.0/32"]
