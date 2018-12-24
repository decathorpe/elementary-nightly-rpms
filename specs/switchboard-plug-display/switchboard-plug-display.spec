%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type hardware
%global plug_name display

%global plug_rdnn io.elementary.switchboard-plug-display

Name:           switchboard-plug-display
Summary:        Switchboard Display plug
Version:        2.1.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
A switchboard plug to show information about displays and to configure
them.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Mon Dec 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.6+git181224.104853.f6664d23-1
- Update to latest snapshot.

* Fri Dec 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.6+git181221.141801.fd6d363d-1
- Update to version 2.1.6.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181219.000749.9ec2680c-1
- Update to latest snapshot.

* Mon Dec 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181217.105402.33bf734f-1
- Update to latest snapshot.

* Sat Dec 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181215.130500.9bdd1540-1
- Update to latest snapshot.

* Thu Dec 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181213.143421.db8e979e-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181212.075229.bddad02d-1
- Update to latest snapshot.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181212.050714.cd412f1b-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.172203.06b0f807-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.145315.aa6737dc-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.121438.712baac7-2
- Adapt to added appdata file.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.071114.d8f3a98a-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.015037.0cd77af1-1
- Update to latest snapshot.

* Tue Dec 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181211.001143.8ba1df6e-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181210.212857.3bd83d02-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181210.203821.810c5f74-1
- Update to latest snapshot.

* Mon Dec 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181210.165744.2cf0ba8d-1
- Update to latest snapshot.

* Sun Dec 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181209.173700.f483ae4b-1
- Update to latest snapshot.

* Sat Dec 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181208.214728.6e83278a-1
- Update to latest snapshot.

* Sun Dec 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181202.063600.e4411b84-1
- Update to latest snapshot.

* Tue Nov 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181127.150346.a19eb3ef-1
- Update to latest snapshot.

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181123.182731.84777b60-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181122.201355.5c58b721-1
- Update to latest snapshot.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181122.083921.dc79d82f-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181117.180609.eabc3835-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181117.092251.099c10a3-1
- Update to latest snapshot.

* Sat Nov 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181117.071652.86a515da-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.185341.d24eced8-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.171831.892c5802-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.160857.434ce226-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.115743.11049582-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.081953.12ce93b4-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.045341.1604d39f-1
- Update to latest snapshot.

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181116.025649.ce74ca9f-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181115.210459.ee702e14-1
- Update to latest snapshot.

* Thu Nov 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181115.191747.ce94aa45-1
- Update to latest snapshot.

* Wed Nov 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181114.133301.d2459dbd-1
- Update to latest snapshot.

* Wed Nov 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181107.015126.305e5753-1
- Update to latest snapshot.

* Tue Nov 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181105.230450.eea4c41d-1
- Update to latest snapshot.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181102.040445.91e91729-2
- Occasional mass rebuild.

* Fri Nov 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181102.040445.91e91729-1
- Update to latest snapshot.

* Mon Oct 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181029.031538.4a2d0937-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181028.172107.7f42142f-1
- Update to latest snapshot.

* Sun Oct 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181028.093451.fd2ad1d7-1
- Update to latest snapshot.

* Fri Oct 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181026.190736.30832119-1
- Update to latest snapshot.

* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181025.080816.196e1f1e-1
- Update to latest snapshot.

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181024.221028.1aa0f744-1
- Update to latest snapshot.

* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181023.220819.e9b08b5a-1
- Update to latest snapshot.

* Mon Oct 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181022.154958.e192b47a-1
- Update to latest snapshot.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181020.215234.407a2f7b-1
- Update to latest snapshot.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181018.001032.e32bcad7-1
- Update to latest snapshot.

* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181017.000728.e06ef695-1
- Update to latest snapshot.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181015.144744.c7ccf759-1
- Update to latest snapshot.

* Sun Oct 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181014.001306.4ff43447-1
- Update to latest snapshot.

* Sat Oct 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181013.121948.b9106568-1
- Update to latest snapshot.

* Fri Oct 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181012.000520.c45a978c-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.173657.894b423f-1
- Update to latest snapshot.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181011.005441.3a315537-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181010.211838.c76b449b-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181010.170958.48c6b252-1
- Update to latest snapshot.

* Wed Oct 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181010.141710.acfa3e95-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.164655.d5841f1f-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.134242.10f4778b-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.092204.1ad28af3-1
- Update to latest snapshot.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181009.015151.f09384d3-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181008.215147.72e271d6-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181008.201956.8590cab9-1
- Update to latest snapshot.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181008.194756.44b05c5a-1
- Update to latest snapshot.

* Thu Oct 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5+git181001.072346.d10358dd-1
- Update to version 2.1.5.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181001.072346.d10358dd-1
- Update to latest snapshot.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git181001.000851.50426cb5-1
- Update to latest snapshot.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180916.180551.93bb86f1-1
- Update to latest snapshot.

* Fri Sep 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180907.000607.01507a3e-1
- Update to latest snapshot.

* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180906.000915.04c14643-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180901.000838.4fd9ea3b-1
- Update to latest snapshot.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180830.000736.2157784d-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180829.062437.20763fb4-1
- Update to latest snapshot.

* Tue Aug 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180828.182818.6bcddd7a-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180823.182208.25acc44b-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180819.000934.6bf9068c-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180815.000905.f3c80943-2
- Occasional mass rebuild.

* Wed Aug 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180815.000905.f3c80943-1
- Update to latest snapshot.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180813.000337.6b2c7b66-1
- Update to latest snapshot.

* Thu Jul 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180726.145600.f7c133e1-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180721.000740.b10dc6d1-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180717.000314.d18a6ce2-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4+git180703.193119.89025527-1
- Update to version 0.1.4.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180703.193119.89025527-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180613.165855.7bc152b7-1
- Update to latest snapshot.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180607.000931.a19f7e6e-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180606.060231.48a99ca6-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180604.024152.42f033e7-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180603.175644.a69189ec-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.195324.7d209e13-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180602.000609.c56775e4-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.144706.fc0f0e7d-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180601.000755.5c2da170-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180531.055228.e5a31d64-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180530.124905.ab4cc85f-1
- Update to latest snapshot.

* Wed May 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180530.091446.8dbe64ad-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.151558.85e9391f-1
- Update to latest snapshot.
- Adapt to upstream file changes.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180529.135235.f529c00e-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.215947.1904f252-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180527.130035.d34d9299-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180511.000618.680fcff9-1
- Update to latest snapshot.

* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180504.000617.52cd5adb-1
- Update to latest snapshot.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180429.142436.619d74f3-1
- Update to latest snapshot.

* Thu Apr 26 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180426.000335.ed966e11-1
- Update to latest snapshot.

* Wed Apr 25 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180425.000334.d06d42ca-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180401.000515.d7ab9837-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180327.000223.e521da68-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180223.182919.ea629027-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180214.203405.5c5bed71-1
- Update to latest snapshot.

* Wed Feb 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180207.033038.6445598e-1
- Update to latest snapshot.

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180205.001145.6b4b5606-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180122.145550.97de7c27-1
- Update to latest snapshot.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180102.234041.dfaae03c-2
- Merge .spec file from fedora.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git180102.234041.dfaae03c-1
- Update to latest snapshot.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171227.174638.840d2ee7-1
- Update to latest snapshot.

* Thu Dec 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171214.173931.79d16a7c-1
- Update to latest snapshot.

* Wed Dec 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171213.051138.523f92a1-1
- Update to latest snapshot.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171212.023220.c3c00ba1-1
- Update to latest snapshot.

* Mon Dec 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171211.224020.178cdcf4-1
- Update to latest snapshot.

* Mon Nov 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171118.231526.4c968719-1
- Update to latest snapshot.

* Sat Oct 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git171027.230155.ae79a6e3-1
- Update to latest snapshot.

* Sat Sep 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170923.185520.f18dcb95-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170817.000741.268df478-1
- Update to latest snapshot.

* Wed Jul 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170712.005905.92447c2c-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170702.180402.110a28c0-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170617.152617.418671fe-1
- Update to latest snapshot.

* Sat Jun 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170603.092900.3f52803d-1
- Update to latest snapshot.

* Wed May 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+git170502.152618.00cc5a7d-1
- Update to version 0.1.3.

* Tue May 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev192-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev191-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev189-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev188-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev187-1
- Update to latest snapshot.

* Wed Feb 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev186-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev185-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev184-1
- Update to latest snapshot.

* Sun Jan 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev183-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev182-1
- Update to latest snapshot.

* Tue Jan 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev181-1
- Update to latest snapshot.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev180-1
- Update to version 0.1.2.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev179-1
- Update to version 0.1.2.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev178-1
- Update to version 0.1.2.1.

* Mon Jan 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev177-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev176-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev175-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.2.1+rev174-1
- Update to version 0.1.2.1.


