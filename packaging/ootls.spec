Name:           ootls
Version:        0.1.0
Release:        1%{?dist}
Summary:        Inspects remote TLS/SSL certificates, cipher suites, expiration, and SAN domains.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootls
Source0:        ootls-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootls is a sovereign, capability-bounded TLS CERT CHECK written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootls
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootls-uninstall

%files
/usr/bin/ootls
/usr/bin/ootls-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
