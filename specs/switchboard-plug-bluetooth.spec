%global debug_package %{nil}

Summary:        Bluetooth plug for Switchboard
Name:           switchboard-plug-bluetooth
Version:        0.1.0+rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-bluetooth

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
A Switchboard plug for configuring Bluetooth.

Built for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-bluetooth-plug


%files -f pantheon-bluetooth-plug.lang
%{_libdir}/switchboard/hardware/pantheon-bluetooth/


%changelog
* Wed Dec 20 2016 Cody Garver <cody@elementary.io> - 0.1.0+rev26-1
- Update to latest snapshot.


