%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-a11y
Summary:        Switchboard Accessibility plug
Version:        0.1.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
The accessibility plug is a section in the Switchboard (System Settings)
that allows the user to manage accessibility settings.


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

%find_lang pantheon-accessibility-plug


%files -f pantheon-accessibility-plug.lang
%doc AUTHORS README.md
%license COPYING

%{_libdir}/switchboard/system/pantheon-accessibility/


%changelog
* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git180209.001034.912e36f8-1
- Update to latest snapshot.

* Sat Jan 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171213.044016.33b965d9-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.230503.f1ce2761-2
- Merge .spec file from fedora.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git171118.230503.f1ce2761-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170731.073728.cac6ed4f-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170711.211554.deda13c2-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170711.211547.b3621378-1
- Update to latest snapshot.

* Fri Jul 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170706.205148.275373aa-1
- Update to latest snapshot.

* Mon Jul 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170703.171056.c89450a1-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170702.185904.1a97c3bc-1
- Update to latest snapshot.

* Thu Jun 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170622.101506.c48b7053-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170617.151523.ae2429ec-1
- Update to latest snapshot.

* Sun May 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170521.211428.bb6c014b-1
- Update to latest snapshot.

* Mon May 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170515.154435.e54d55cc-1
- Update to latest snapshot.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+git170507.203006.a63cdbcf-1
- Update to version 0.1.1.

* Mon May 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev140-1
- Update to latest snapshot.

* Sun Apr 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev139-1
- Update to latest snapshot.

* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev138-1
- Update to latest snapshot.

* Sun Apr 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev137-1
- Update to latest snapshot.

* Mon Mar 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev135-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev133-1
- Update to latest snapshot.

* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev132-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev127-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev126-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev125-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev124-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev123-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev122-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev121-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev120-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev119-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev118-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev117-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev116-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev115-1
- Update to version 0.1.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev114-1
- Update to version 0.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev113-1
- Update to version 0.1.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev112-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev111-1
- Update to latest snapshot.

* Wed Dec 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev110-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev109-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev108-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev107-1
- Update to latest snapshot.

* Fri Nov 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev106-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1+rev105-1
- Update to version 0.1.


