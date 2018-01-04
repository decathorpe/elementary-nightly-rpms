%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-networking
Summary:        Switchboard Networking plug
Version:        0.1.1+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libnm-gtk)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    (switchboard%{?_isa} and NetworkManager%{?_isa})


%description
A switchboard plug for configuring available networks.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-network-plug


%files -f pantheon-network-plug.lang
%doc AUTHORS README.md
%license COPYING

%{_libdir}/switchboard/network/pantheon-network/


%changelog
* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180103.010504.5910cd45-1
- Update to latest snapshot.

* Sat Dec 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171229.230757.cfa74410-1
- Update to latest snapshot.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171227.173136.e1bb1bc5-1
- Update to latest snapshot.

* Tue Dec 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171226.174250.53810d6a-1
- Update to latest snapshot.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-2
- Adapt to upstream dependency changes.

* Sun Dec 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171222.220023.5a5867be-1
- Update to latest snapshot.

* Wed Dec 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171220.181623.c8ca88b0-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.235353.8e23d341-1
- Update to latest snapshot.

* Fri Nov 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171117.184103.adae98e2-1
- Update to latest snapshot.

* Thu Nov 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171102.164146.382f335a-1
- Update to latest snapshot.

* Fri Oct 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171027.154651.d36d298f-1
- Update to latest snapshot.

* Thu Oct 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171026.172718.a8b97c55-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171025.143830.b20434d6-1
- Update to latest snapshot.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.181951.59b079bd-1
- Update to latest snapshot.

* Tue Oct 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171024.000054.03d3091f-1
- Update to latest snapshot.

* Mon Oct 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171023.183001.c7e0308a-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.185929.b49a6155-1
- Update to latest snapshot.

* Mon Oct 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171002.143240.914b8935-1
- Update to latest snapshot.

* Fri Sep 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170922.000642.b649a59f-1
- Update to latest snapshot.

* Sat Sep 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170916.000221.e500be8d-1
- Update to latest snapshot.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170915.095826.284e1174-1
- Update to version 0.1.1.

* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev504-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev503-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev501-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev495-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev491-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev490-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev384-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev383-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev382-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev381-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev380-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev379-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev378-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev377-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev376-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev375-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev374-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev373-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev372-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev371-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev370-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev369-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev368-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev367-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev366-1
- Update to version 0.1.0.3.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev365-1
- Update to version 0.1.0.3.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev364-1
- Update to version 0.1.0.3.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev363-1
- Update to version 0.1.0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev362-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev361-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev360-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev359-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev356-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev354-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev353-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev352-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev351-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev350-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev349-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev348-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev347-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev346-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev345-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev344-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev343-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev342-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev341-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev340-1
- Update to version 0.1.0.3.


