%define src_name ipxe

Summary: iPXE source archive
Name: ipxe-source
Version: 1
Release: 1%{dist}
License: GPLv2
Patch0: makefile.patch
Patch1: ipxe-eb5a2ba5962579e514b377f5fdab7292be0fb2a7.patch
Patch2: ipxe-9df238a8aa1c6074f98280d9dfa08c4ea7e1ff86.patch
Patch3: ipxe-66ea4581256449fe9dcb26340851c09ffd9d6290.patch
Patch4: 0001-dhcp-Check-for-matching-chaddr-in-received-DHCP-pack.patch
Patch5: 0001-pxe-Maintain-a-queue-for-received-PXE-UDP-packets.patch
Patch6: pxe-tftp-load-from-program-pxecall.patch
Patch7: ipxe-do-not-implement-UNDI-GET_NEXT-if-PVS.patch
Patch8: ipxe-udp-write-blocking.patch
Patch9: ipxe-no-post-prompt.patch
Patch10: 0001-dhcp-Remove-obsolete-dhcp_chaddr-function.patch
Patch11: 0002-dhcp-Allow-pseudo-DHCP-servers-to-use-pseudo-identif.patch
Patch12: 0003-dhcp-Ignore-ProxyDHCPACKs-without-PXE-options.patch
Patch13: 0004-dhcp-Do-not-skip-ProxyDHCPREQUEST-if-next-server-is-.patch
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{src_name}/archive?at=a712dae709a&format=tar.gz&prefix=%{src_name}-%{version}#/%{src_name}-%{version}.tar.gz
BuildArch: noarch

%description
Ipxe specfile

%prep
%autosetup -p1 -n %{src_name}-%{version} -n ipxe-1

%build
mkdir -p ../%{src_name}
find . | cpio -pdmv ../%{src_name}

%install
mkdir -p %{buildroot}%{_usrsrc}
tar zcvf %{buildroot}%{_usrsrc}/%{name}.tar.gz -C .. %{src_name}

%files
%{_usrsrc}/%{name}.tar.gz
