Name:		system-setup-keyboard
Version:	0.7
Release:	4%{?dist}
Summary:	Hal keyboard layout callout

Group:		Applications/System
License:	MIT
URL:		http://git.fedorahosted.org/git/system-setup-keyboard.git/
Source0:	https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	hal-devel
BuildRequires:	glib2-devel
BuildRequires:	system-config-keyboard

Requires:	hal
Conflicts:	xorg-x11-server-Xorg < 1.6.0-7

Provides:	fedora-setup-keyboard = %{version}-%{release}
Obsoletes:	fedora-setup-keyboard < 0.7

# 572787
Patch1:		system-setup-keyboard-0.7-man-page.patch
Patch2:		system-setup-keyboard-0.7-help-output.patch
# Bug 595654 - GDM Does Not Respect Installation Time Keyboard Choice 
Patch3:         system-setup-keyboard-0.7-all-keyboards.patch

%description
%{name} gets invoked by hal to apply the keyboard layout
defined in /etc/sysconfig/keyboard.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/hal/fdi/policy/10osvendor/10-x11-keymap.fdi
%doc COPYING
%{_mandir}/man1/system-setup-keyboard.1*

%changelog
* Wed Jun 09 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.7-4
- system-setup-keyboard-0.7-all-keyboards.patch: apply keyboard layout to
  all key devices, not just those with input.keyboard capabilities (#595654).

* Fri Mar 19 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.7-3
- Add --help output (#572787)

* Fri Mar 12 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.7-2
- Add a man page. (#572787)

* Tue Feb 09 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.7-1
- Rename to system-setup-keyboard, update the URL and Source0 accordingly.
  Obsoletes fedora-setup-keyboard.

* Sat Dec 26 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.6-1
- 0.6 release
- Fixes RH #545970

* Fri Nov 20 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.5-1
- Patch merged upstream

* Fri Nov 20 2009 Peter Hutterer <peter.hutterer@redhat.com> 0.4-4
- rhpl was replaced by system-config-keyboard.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 27 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.4-2
- Rebuild to pick up rhpl changes

* Mon Apr 13 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.4-1
- 0.4 release
- Dropped patch, merged upstream

* Thu Apr 09 2009 Peter Hutterer <peter.hutterer@redhat.com> 0.3-4
- fedora-setup-keyboard-0.3-merge-terminate.patch: merge xkb options for
  termination.

* Thu Mar 05 2009 Peter Hutterer <peter.hutterer@redhat.com> 0.3-3
- Conflict xorg-x11-server-Xorg < 1.6.0-7 (10-x11-keymap.fdi and
  fedora-setup-keyboard up to 1.6.0-5)

* Mon Mar 02 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.3-2
- Fix license tag

* Wed Feb 25 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.3-1
- 0.3 release
- Require hal

* Sat Feb 21 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.2-1
- Initial package
