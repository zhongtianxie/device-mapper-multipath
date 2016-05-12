Summary: Tools to manage multipath devices using device-mapper
Name: device-mapper-multipath
Version: 0.4.9
Release: 85%{?dist}.2
License: GPL+
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/

Source0: multipath-tools-130222.tgz
Source1: multipath.conf
Patch0001: 0001-RH-dont_start_with_no_config.patch
Patch0002: 0002-RH-multipath.rules.patch
Patch0003: 0003-RH-Make-build-system-RH-Fedora-friendly.patch
Patch0004: 0004-RH-multipathd-blacklist-all-by-default.patch
Patch0005: 0005-RH-add-mpathconf.patch
Patch0006: 0006-RH-add-find-multipaths.patch
Patch0007: 0007-RH-add-hp_tur-checker.patch
Patch0008: 0008-RH-revert-partition-changes.patch
Patch0009: 0009-RH-RHEL5-style-partitions.patch
Patch0010: 0010-RH-dont-remove-map-on-enomem.patch
Patch0011: 0011-RH-deprecate-uid-gid-mode.patch
Patch0012: 0012-RH-kpartx-msg.patch
Patch0013: 0013-RHBZ-883981-cleanup-rpmdiff-issues.patch
Patch0014: 0014-RH-handle-other-sector-sizes.patch
Patch0015: 0015-RH-fix-output-buffer.patch
Patch0016: 0016-RH-dont-print-ghost-messages.patch
#Patch0017: 0017-RH-fix-sigusr1.patch
Patch0018: 0018-RH-fix-factorize.patch
Patch0019: 0019-RH-fix-sockets.patch
Patch0020: 0020-RHBZ-907360-static-pthread-init.patch
Patch0021: 0021-RHBZ-919119-respect-kernel-cmdline.patch
Patch0022: 0022-RH-multipathd-check-wwids.patch
Patch0023: 0023-RH-multipath-wipe-wwid.patch
Patch0024: 0024-RH-multipath-wipe-wwids.patch
Patch0025: 0025-UPBZ-916668_add_maj_min.patch
Patch0026: 0026-fix-checker-time.patch
Patch0027: 0027-RH-get-wwid.patch
Patch0028: 0028-RHBZ-929078-refresh-udev-dev.patch
Patch0029: 0029-RH-no-prio-put-msg.patch
Patch0030: 0030-RHBZ-916528-override-queue-no-daemon.patch
Patch0031: 0031-RHBZ-957188-kpartx-use-dm-name.patch
Patch0032: 0032-RHBZ-956464-mpathconf-defaults.patch
Patch0033: 0033-RHBZ-829963-e-series-conf.patch
Patch0034: 0034-RHBZ-851416-mpathconf-display.patch
Patch0035: 0035-RHBZ-891921-list-mpp.patch
Patch0036: 0036-RHBZ-949239-load-multipath-module.patch
Patch0037: 0037-RHBZ-768873-fix-rename.patch
Patch0038: 0038-RHBZ-799860-netapp-config.patch
Patch0039: 0039-RH-detect-prio-fix.patch
Patch0040: 0040-RH-bindings-fix.patch
Patch0041: 0041-RH-check-for-erofs.patch
Patch0042: 0042-UP-fix-signal-handling.patch
Patch0043: 0043-RH-signal-waiter.patch
Patch0044: 0044-RHBZ-976688-fix-wipe-wwids.patch
Patch0045: 0045-RHBZ-977297-man-page-fix.patch
Patch0046: 0046-RHBZ-883981-move-udev-rules.patch
Patch0047: 0047-RHBZ-kpartx-read-only-loop-devs.patch
Patch0048: 0048-RH-print-defaults.patch
Patch0049: 0049-RH-remove-ID_FS_TYPE.patch
Patch0050: 0050-RH-listing-speedup.patch
Patch0051: 0051-UP-fix-cli-resize.patch
Patch0052: 0052-RH-fix-bad-derefs.patch
Patch0053: 0053-UP-fix-failback.patch
Patch0054: 0054-UP-keep-udev-ref.patch
Patch0055: 0055-UP-handle-quiesced-paths.patch
Patch0056: 0056-UP-alua-prio-fix.patch
Patch0057: 0057-UP-fix-tmo.patch
Patch0058: 0058-UP-fix-failback.patch
Patch0059: 0059-UP-flush-failure-queueing.patch
Patch0060: 0060-UP-uevent-loop-udev.patch
Patch0061: 0061-RH-display-find-mpaths.patch
Patch0062: 0062-RH-dont-free-vecs.patch
Patch0063: 0063-RH-fix-warning.patch
Patch0064: 0064-RHBZ-1010040-fix-ID_FS-attrs.patch
Patch0065: 0065-UPBZ-995538-fail-rdac-on-unavailable.patch
Patch0066: 0066-UP-dos-4k-partition-fix.patch
Patch0067: 0067-RHBZ-1022899-fix-udev-partition-handling.patch
Patch0068: 0068-RHBZ-1034578-label-partition-devices.patch
Patch0069: 0069-UPBZ-1033791-improve-rdac-checker.patch
Patch0070: 0070-RHBZ-1036503-blacklist-td-devs.patch
Patch0071: 0071-RHBZ-1031546-strip-dev.patch
Patch0072: 0072-RHBZ-1039199-check-loop-control.patch
Patch0073: 0073-RH-update-build-flags.patch
Patch0074: 0074-RHBZ-1056976-dm-mpath-rules.patch
Patch0075: 0075-RHBZ-1056976-reload-flag.patch
Patch0076: 0076-RHBZ-1056686-add-hw_str_match.patch
Patch0077: 0077-RHBZ-1054806-mpathconf-always-reload.patch
Patch0078: 0078-RHBZ-1054044-fix-mpathconf-manpage.patch
Patch0079: 0079-RHBZ-1070581-add-wwid-option.patch
Patch0080: 0080-RHBZ-1075796-cmdline-wwid.patch
Patch0081: 0081-RHBZ-1066264-check-prefix-on-rename.patch
Patch0082: 0082-UPBZ-1109995-no-sync-turs-on-pthread_cancel.patch
Patch0083: 0083-RHBZ-1080055-orphan-paths-on-reload.patch
Patch0084: 0084-RHBZ-1110000-multipath-man.patch
Patch0085: 0085-UPBZ-1110006-datacore-config.patch
Patch0086: 0086-RHBZ-1110007-orphan-path-on-failed-add.patch
Patch0087: 0087-RHBZ-1110013-config-error-checking.patch
Patch0088: 0088-RHBZ-1069811-configurable-prio-timeout.patch
Patch0089: 0089-RHBZ-1110016-add-noasync-option.patch
Patch0090: 0090-UPBZ-1080038-reorder-paths-for-round-robin.patch
Patch0091: 0091-RHBZ-1069584-fix-empty-values-fast-io-fail-and-dev-loss.patch
Patch0092: 0092-UPBZ-1104605-reload-on-rename.patch
Patch0093: 0093-UPBZ-1086825-user-friendly-name-remap.patch
Patch0094: 0094-RHBZ-1086825-cleanup-remap.patch
Patch0095: 0095-RHBZ-1127944-xtremIO-config.patch
Patch0096: 0096-RHBZ-979474-new-wildcards.patch
Patch0097: 0097-RH-fix-coverity-errors.patch
Patch0098: 0098-UPBZ-1067171-mutipath-i.patch
Patch0099: 0099-RH-add-all-devs.patch
Patch0100: 0100-RHBZ-1067171-multipath-i-update.patch
Patch0101: 0101-RH-cleanup-partmaps-code.patch
Patch0102: 0102-RHBZ-631009-deferred-remove.patch
Patch0103: 0103-RHBZ-1148979-fix-partition-mapping-creation-race-with-kpartx.patch
Patch0104: 0104-RHBZ-1159337-fix-double-free.patch
Patch0105: 0105-RHBZ-1180032-find-multipaths-man.patch
Patch0106: 0106-RHBZ-1169935-no-new-devs.patch
Patch0107: 0107-RH-adapter-name-wildcard.patch
Patch0108: 0108-RHBZ-1153832-kpartx-remove-devs.patch
Patch0109: 0109-RH-read-only-bindings.patch
Patch0110: 0110-RHBZ-blacklist-vd-devs.patch
Patch0111: 0111-RH-dont-show-pg-timeout.patch
Patch0112: 0112-RHBZ-1194917-add-config_dir-option.patch
Patch0113: 0113-RHBZ-1194917-cleanup.patch
Patch0114: 0114-RHBZ-1196394-delayed-reintegration.patch
Patch0115: 0115-RHBZ-1198418-fix-double-free.patch
Patch0116: 0116-UPBZ-1188179-dell-36xxi.patch
Patch0117: 0117-RHBZ-1198424-autodetect-clariion-alua.patch
Patch0118: 0118-UPBZ-1200738-update-eternus-config.patch
Patch0119: 0119-RHBZ-1081397-save-alua-info.patch
Patch0120: 0120-RHBZ-1043093-realloc-fix.patch
Patch0121: 0121-RHBZ-1197234-rules-fix.patch
Patch0122: 0122-RHBZ-1212590-dont-use-var.patch
Patch0123: 0123-UPBZ-1166072-fix-path-offline.patch
Patch0124: 0124-RHBZ-1209275-retrigger-uevents.patch
Patch0125: 0125-RHBZ-1153832-kpartx-delete.patch
Patch0126: 0126-RHBZ-1211383-alias-collision.patch
Patch0127: 0127-RHBZ-1201030-use-blk-availability.patch
Patch0128: 0128-RHBZ-1222123-mpathconf-allow.patch
Patch0129: 0129-UPBZ-1254292-iscsi-targetname.patch
Patch0130: 0130-RHBZ-1259523-host_name_len.patch
Patch0131: 0131-UPBZ-1259831-lock-retry.patch
Patch0132: 0132-RHBZ-1296979-fix-define.patch
Patch0133: 0133-RHBZ-1321019-wait-for-map-add.patch

# runtime
Requires: %{name}-libs = %{version}-%{release}
Requires: kpartx = %{version}-%{release}
Requires: device-mapper >= 7:1.02.96
Requires: initscripts
Requires(post): systemd-units systemd-sysv chkconfig
Requires(preun): systemd-units
Requires(postun): systemd-units

# build/setup
BuildRequires: libaio-devel, device-mapper-devel >= 1.02.89
BuildRequires: libselinux-devel, libsepol-devel
BuildRequires: readline-devel, ncurses-devel
BuildRequires: systemd-units, systemd-devel

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package libs
Summary: The %{name} modules and shared library
License: GPL+
Group: System Environment/Libraries

%description libs
The %{name}-libs provides the path checker
and prioritizer modules. It also contains the multipath shared library,
libmultipath.

%package sysvinit
Summary: SysV init script for device-mapper-multipath
Group: System Environment/Libraries

%description sysvinit
SysV style init script for device-mapper-multipth. It needs to be
installed only if systemd is not used as the system init process.

%package -n kpartx
Summary: Partition device manager for device-mapper devices
Group: System Environment/Base

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%prep
%setup -q -n multipath-tools-130222
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
# %%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1
%patch0089 -p1
%patch0090 -p1
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
cp %{SOURCE1} .

%build
%define _sbindir /usr/sbin
%define _libdir /usr/%{_lib}
%define _libmpathdir %{_libdir}/multipath
make %{?_smp_mflags} LIB=%{_lib}

%install
rm -rf %{buildroot}

make install \
	DESTDIR=%{buildroot} \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	libdir=%{_libmpathdir} \
	rcdir=%{_initrddir} \
	unitdir=%{_unitdir}

# tree fix up
install -d %{buildroot}/etc/multipath

%clean
rm -rf %{buildroot}

%post
%systemd_post multipathd.service

%preun
%systemd_preun multipathd.service

%postun
if [ $1 -ge 1 ] ; then
	/sbin/multipathd forcequeueing daemon > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart multipathd.service

%triggerun -- %{name} < 0.4.9-37
# make sure old systemd symlinks are removed after changing the [Install]
# section in multipathd.service from multi-user.target to sysinit.target
/bin/systemctl --quiet is-enabled multipathd.service >/dev/null 2>&1 && /bin/systemctl reenable multipathd.service ||:

%triggerun --  %{name} < 0.4.9-16
%{_bindir}/systemd-sysv-convert --save multipathd >/dev/null 2>&1 ||: 
bin/systemctl --no-reload enable multipathd.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del multipathd >/dev/null 2>&1 || :
/bin/systemctl try-restart multipathd.service >/dev/null 2>&1 || :

%triggerpostun -n %{name}-sysvinit -- %{name} < 0.4.9-16
/sbin/chkconfig --add mdmonitor >/dev/null 2>&1 || :

%files
%defattr(-,root,root,-)
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/mpathconf
%{_sbindir}/mpathpersist
%{_unitdir}/multipathd.service
%{_mandir}/man3/mpath_persistent_reserve_in.3.gz
%{_mandir}/man3/mpath_persistent_reserve_out.3.gz
%{_mandir}/man5/multipath.conf.5.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%{_mandir}/man8/mpathconf.8.gz
%{_mandir}/man8/mpathpersist.8.gz
%config /usr/lib/udev/rules.d/62-multipath.rules
%config /usr/lib/udev/rules.d/11-dm-mpath.rules
%doc AUTHOR COPYING FAQ
%doc multipath.conf
%dir /etc/multipath

%files libs
%defattr(-,root,root,-)
%doc AUTHOR COPYING
%{_libdir}/libmultipath.so
%{_libdir}/libmultipath.so.*
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathpersist.so.*
%dir %{_libmpathdir}
%{_libmpathdir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files sysvinit
%{_initrddir}/multipathd

%files -n kpartx
%defattr(-,root,root,-)
%{_sbindir}/kpartx
%{_mandir}/man8/kpartx.8.gz

%changelog
* Mon Mar 28 2016 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-85.2
- Add 0133-RHBZ-1321019-wait-for-map-add.patch
  * wait for the device to finish being added before reloading it.
- Resolves: bz #1321019

* Mon Feb 01 2016 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-85.1
- Add 0132-RHBZ-1296979-fix-define.patch
  * look for the correct libudev function to set define
- Resolves: bz #1303623

* Thu Sep 17 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-85
- Fix device-mapper Requires line in spec file
- Resolves: bz# 1260728

* Mon Sep 14 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-84
- 0131-UPBZ-1259831-lock-retry.patch
  * retry locking when creating multipath devices
- Resolves: bz# 1259831

* Tue Sep  8 2015 Benjmain Marzinski <bmarzins@redhat.com> 0.4.9-83
- Add 0130-RHBZ-1259523-host_name_len.patch
  * increase size of host string
- Resolves: bz# 1259523

* Wed Aug 19 2015 Benjmain Marzinski <bmarzins@redhat.com> 0.4.9-82
- Add 0129-UPBZ-1254292-iscsi-targetname.patch
  * check for targetname iscsi sysfs value
- Resolves: bz #1254292

* Wed Jul  8 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-81
- Modify 0128-RHBZ-1222123-mpathconf-allow.patch
  * Fix up covscan complaints.
- Related: bz #1222123

* Tue Jul  7 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-80
- Add 0127-RHBZ-1201030-use-blk-availability.patch
  * Make multipath use blk-availability.service
- Add 0128-RHBZ-1222123-mpathconf-allow.patch
  * Add mpathconf --allow for creating specialized config files.
- Resolves: bz #1201030, #1222123

* Fri Jun  5 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-79
- Add 0124-RHBZ-1209275-retrigger-uevents.patch
  * Make multipathd retrigger uevents when paths haven't successfully had
    their udev_attribute environment variable set by udev and add
    "retrigger_ties" and "retrigger_delay" to control this
- Add 0125-RHBZ-1153832-kpartx-delete.patch
  * Delete all partition devices with -d (not just the ones in the partition
    table)
- Add 0126-RHBZ-1211383-alias-collision.patch
  * make multipathd use the old alias, if rename failed and add
    "new_bindings_in_boot" to determine if new bindings can be added to
    the bindings file in the initramfs
- Resolves: bz #1153832, #1209275, #1211383

* Thu May  7 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-78
- Modify 0102-RHBZ-631009-deferred-remove.patch
  * Code refactor and minor fix.
- Add 0106-RHBZ-1169935-no-new-devs.patch
  * add new configuration option "ignore_new_boot_devs"
- Add 0107-RH-adapter-name-wildcard.patch
  * add new paths wildcard to show the host adapter
- Add 0108-RHBZ-1153832-kpartx-remove-devs.patch
  * switch to kpartx -u in 62-multipath.rules to delete removed partitions
- Add 0109-RH-read-only-bindings.patch
  * add -B support to multipathd
- Add 0110-RHBZ-blacklist-vd-devs.patch
  * virtio-blk devices don't report a WWID so multipath can't use them
- Add 0111-RH-dont-show-pg-timeout.patch
  * remove pg_timeout setting and displaying code
- Add 0112-RHBZ-1194917-add-config_dir-option.patch
  * add new configuration option "config_dir"
- Add 0113-RHBZ-1194917-cleanup.patch
  * code refactoring
- Add 0114-RHBZ-1196394-delayed-reintegration.patch
  * add new configuration options "delay_watch_checks" and
    "delay_wait_checks"
- Add 0115-RHBZ-1198418-fix-double-free.patch
  * fix crash when multipath fails adding a multipath device
- Add 0116-UPBZ-1188179-dell-36xxi.patch
  * New builtin config
- Add 0117-RHBZ-1198424-autodetect-clariion-alua.patch
  * update default config
- Add 0118-UPBZ-1200738-update-eternus-config.patch
  * update default config
- Add 0119-RHBZ-1081397-save-alua-info.patch
  * make prioritizers save information between calls to speed them up.
- Add 0120-RHBZ-1043093-realloc-fix.patch
  * free old memory if realloc fails.
- Add 0121-RHBZ-1197234-rules-fix.patch
  * make sure kpartx runs after an DM_ACTIVATION event occurs.
- Add 0122-RHBZ-1212590-dont-use-var.patch
  * use /run instead of /var/run
- Add 0123-UPBZ-1166072-fix-path-offline.patch
  * Don't mark quiesce and transport-offline paths as offline
- Modify mulfipth.conf default config file (bz #1194794)
- Related: bz #1153832
- Resolves: bz #631009, #1043093, #1081397, #1166072, #1169935, #1188179
- Resolves: bz #1194794, #1194917, #1196394, #1197234, #1198418, #1198424
- Resolves: bz #1200738, #1212590

* Fri Jan  9 2015 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-77
- Add 0105-RHBZ-1180032-find-multipaths-man.patch
  * add find_multipaths to man page
- Modify multipath.conf (bz #1069360)
  * add uid_attribute example
- Resolves: bz #1180032

* Fri Nov 14 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-76
- Modify 0102-RHBZ-631009-deferred-remove.patch
  * Fixed compiler warning message for builds with old device-mapper versions
- Add 0104-RHBZ-1159337-fix-double-free.patch
  * made ev_remove_path exit immediately after failing setup_multipath, since
    it handles cleaning up the device
- Resolves: bz #1159337
- Related: bz #631009

* Thu Nov  6 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-75
- Add 0103-RHBZ-1148979-fix-partition-mapping-creation-race-with-kpartx.patch
  * Only run kpartx on device activation
- Resolves: bz #1148979

* Tue Oct 28 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-74
- Respin again to let buildroot catch up.
- Related: bz #631009

* Tue Oct 28 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-73
- Respin to pick up latest lvm2 code
- Related: bz #631009

* Tue Oct 28 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-72
- Add 0101-RH-cleanup-partmaps-code.patch
  * code refactoring to prepare for next patch
- Add 0102-RHBZ-631009-deferred-remove.patch
  * add deferred_remove option to /etc/multipath.conf
- Resolves: bz #631009

* Fri Sep  5 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-71
- Re-add 0050-RH-listing-speedup.patch
- Modify 0098-UPBZ-1067171-mutipath-i.patch
  * add dry_run cleanup code from upstream
- Refresh 0099-RH-add-all-devs.patch
- Add 0100-RHBZ-1067171-multipath-i-update.patch
  * make -i work correctly with find_multipaths
- Resolves: bz #1067171

* Wed Sep  3 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-70
- Modify 0096-RHBZ-979474-new-wildcards.patch
  * Fix a faulty check
- Add 0098-UPBZ-1067171-mutipath-i.patch
  * Add -i option to ignore wwids file when checking for valid paths
- Add 0099-RH-add-all-devs.patch
  * Add new devices config option all_devs. This makes the configuration
    overwrite the specified values in all builtin configs
- Related: bz #979474
- Resolves: bz #1067171

* Thu Aug 28 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-69
- Add 0096-RHBZ-979474-new-wildcards.patch
  * Add N, n, R, and r path wildcards to print World Wide ids
- Add 0097-RH-fix-coverity-errors.patch
  * Fix a number of unterminated strings and memory leaks on failure
    paths.
- Resolves: bz #979474

* Tue Aug 12 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-68
- Add 0091-RHBZ-1069584-fix-empty-values-fast-io-fail-and-dev-loss.patch
  * check for null pointers in configuration reading code.
- Add 0092-UPBZ-1104605-reload-on-rename.patch
  * Reload table on rename if necessary
- Add 0093-UPBZ-1086825-user-friendly-name-remap.patch
  * Keep existing user_friend_name if possible
- Add 0094-RHBZ-1086825-cleanup-remap.patch
  * Cleanup issues with upstream patch
- Add 0095-RHBZ-1127944-xtremIO-config.patch
  * Add support for EMC ExtremIO devices
- Resolves: bz #1069584, #1104605, #1086825, #1086825, #1127944

* Tue Aug 12 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-67
- Modify multipath.conf (bz #1069360)
  * remove getuid_callout example
- Add 0081-RHBZ-1066264-check-prefix-on-rename.patch
  * make multipath check the prefix on kpartx partitions during rename, and
    copy the existing behaviour
- Add 0082-UPBZ-1109995-no-sync-turs-on-pthread_cancel.patch
  * If async tur checker fails on threads, don't retry with the sync version
- Add 0083-RHBZ-1080055-orphan-paths-on-reload.patch
  * Fix case where pathlist wasn't getting updated properly
- Add 0084-RHBZ-1110000-multipath-man.patch
  * fix errors in multipath man page
- Add 0085-UPBZ-1110006-datacore-config.patch
  * Add support for DataCore Virtual Disk
- Add 0086-RHBZ-1110007-orphan-path-on-failed-add.patch
  * If multipathd fails to add path correctly, it now fully orphans the path
- Add 0087-RHBZ-1110013-config-error-checking.patch
  * Improve multipath.conf error checking.
- Add 0088-RHBZ-1069811-configurable-prio-timeout.patch
  * checker_timeout now adjusts the timeouts of the prioritizers as well.
- Add 0089-RHBZ-1110016-add-noasync-option.patch
  * Add a new defaults option, "force_sync", that disables the async mode
    of the path checkers. This is for cases where to many parallel checkers
    hog the CPU
- Add 0090-UPBZ-1080038-reorder-paths-for-round-robin.patch
  * make multipathd order paths for better throughput in round-robin mode
- Resolves: bz #1069360, #1066264, #1109995, #1080055, #1110000, #1110006
- Resolves: bz #1110007, #1110013, #1069811, #1110016, #1080038

* Wed Mar 12 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-66
- Add 0080-RHBZ-1075796-cmdline-wwid.patch
  * add multipath option "-A" to add wwids specified by the kernel
    command line mapth.wwid options.
- Resolves: bz #1075796

* Mon Mar  3 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-65
- Add 0078-RHBZ-1054044-fix-mpathconf-manpage.patch
  * Fix typo
- Add 0079-RHBZ-1070581-add-wwid-option.patch
  * add multipath option "-a". To add a device's wwid to the wwids file
- Resolves: bz #1054044, #1070581

* Thu Jan 30 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-64
- Modify 0076-RHBZ-1056686-add-hw_str_match.patch
  * Fix memory leak
- Resolves: bz #1056686

* Wed Jan 29 2014 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-63
- Modify 0072-RHBZ-1039199-check-loop-control.patch
  * only call close on the /dev/loop-control fd the open succeeds
- Add 0073-RH-update-build-flags.patch
  * fix print call to work with -Werror=format-security compile flag, and
    change compilation flags for non-rpmbuild compiles
- Add 0074-RHBZ-1056976-dm-mpath-rules.patch
  * Add rules to keep from doing work in udev if there are no
    active paths, or if the event was for a multipath device
    reloading its table due to a path change.
- Add 0075-RHBZ-1056976-reload-flag.patch
  * multipath code to identify reloads that the new rules can
    ignore
- Add 0076-RHBZ-1056686-add-hw_str_match.patch
  * add a new default config paramter, "hw_str_match", to make user
    device configs only overwrite builtin device configs if the
    identifier strings match exactly, like the default in RHEL6.
- Add 0077-RHBZ-1054806-mpathconf-always-reload.patch
  * Make mpathconf always reconfgure multipathd when you run it with
    a reconfigure option and --with-multipathd=y, even if the
    configuration doesn't change.
- Update Requires and BuildRequires for device-mapper to 1.02.82-2
- Install new udev rules file /usr/lib/udev/rules.d/11-dm-mpath.rules
- Related: bz #1039199
- Resolves: bz #1054806, #1056686, #1056976

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.4.9-62
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.9-61
- Mass rebuild 2013-12-27

* Wed Dec 11 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-60
- Add 0072-RHBZ-1039199-check-loop-control.patch
  * Make kpartx use LOOP_CTL_GET_FREE and loop-control to find a free
    loop device. This will autoload the loop module.
- Resolves: bz #1039199

* Mon Dec  9 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-59
- Add 0067-RHBZ-1022899-fix-udev-partition-handling.patch
  * Make sure to wipe partition devices on change event if they weren't 
    wiped on the device add event 
- Add 0068-RHBZ-1034578-label-partition-devices.patch   
  * Make sure that partition devices are labeled like the whole device 
- Add 0069-UPBZ-1033791-improve-rdac-checker.patch   
  *  Use RTPG data in RDAC checker 
- Add 0070-RHBZ-1036503-blacklist-td-devs.patch
- Add 0071-RHBZ-1031546-strip-dev.patch   
  * make multipathd interactive commands able to handle /dev/<devnode> 
    instead of just <devnode>
- Resolves: bz #1022899, #1031546, #1033791, #1034578, #1036503 

* Thu Oct 24 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-58
- 0066-UP-dos-4k-partition-fix.patch
  * Make kpartx correctly handle 4K sector size devices with dos partitions.
- Resolves: bz #1018439 

* Fri Sep 27 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-57
- Add 0065-UPBZ-995538-fail-rdac-on-unavailable.patch
  * make rdac checker always mark paths with asymmetric access state of
    unavailable as down
- Resolves: bz #995538

* Wed Sep 25 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-56
- Add 0064-RHBZ-1010040-fix-ID_FS-attrs.patch
  * make multipath create a timestamp file /run/multipathd/timestamp, and
    add -T<timestamp>:<valid> option to shortcut processing if the
    timestamp hasn't changed
- Resolves: bz #1010040

* Fri Sep  6 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-55
- Add 0061-RH-display-find-mpaths.patch
- Add 0062-RH-dont-free-vecs.patch
  * freeing vecs causes a number of races which can crash multipathd on
    shutdown.
- Add 0063-RH-fix-warning.patch

* Thu Jul 25 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-54
- Modify 0015-RH-fix-output-buffer.patch
  * Fix memory leak
- Add 0047-RHBZ-kpartx-read-only-loop-devs.patch
  * Fix read only loop device handling
- Add 0048-RH-print-defaults.patch
- Add 0049-RH-remove-ID_FS_TYPE.patch
  * remove ID_FS_TYPE udev enviroment variable for multipath devices
- Add 0051-UP-fix-cli-resize.patch
  * check before dereferencing variables
- Add 0052-RH-fix-bad-derefs.patch
  * setup multipath free the multipath device when it fails, so don't keep
    using it.
- Add 0053-UP-fix-failback.patch
  * setting failback in the devices section was broken
- Add 0054-UP-keep-udev-ref.patch
  * multipathd needs to keep the same udev object across reconfigures
- Add 0055-UP-handle-quiesced-paths.patch
  * quiesced paths should be treated as down
- Add 0056-UP-alua-prio-fix.patch
  * Don't count the preferred bit for paths that are active/optimized
- Add 0057-UP-fix-tmo.patch
  * Cleanup how multipath sets dev_loss_tmo and fast_io_fail_tmo.  Also
    make multipath get changing values directly from sysfs, instead of
    from udev, which caches them.
- Add 0058-UP-fix-failback.patch
  * make failback print the default value when you show configs.
- Add 0059-UP-flush-failure-queueing.patch
  * If you can't flush a multipath device, restore the queue_if_no_paths
    value
- Add 0060-UP-uevent-loop-udev.patch
  * make ueventloop grab it's own udev reference, since it is cancelled
    asychnrously.

* Wed Jul  3 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-53
- Add 0044-RHBZ-976688-fix-wipe-wwids.patch
  * Seek back to the start of the file after truncating it
- Add 0045-RHBZ-977297-man-page-fix.patch
  * update man page to match actual defaults
- Add 0046-RHBZ-883981-move-udev-rules.patch
  * move udev rules file from /lib to /usr/lib
- Resolves: bz #883981, #976688, #977297

* Fri Jun 21 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-52
- Add 0038-RHBZ-799860-netapp-config.patch
- Add 0039-RH-detect-prio-fix.patch
  * Don't autodetect ALUA prioritizer unless it actually can get a priority
- Add 0040-RH-bindings-fix.patch
  * Do a better job of trying to get the first free user_friendly_name
- Add 0041-RH-check-for-erofs.patch
  * Don't create/reload a device read-only unless doing it read/write fails
    with EROFS
- Remove 0017-RH-fix-sigusr1.patch
  * fix signal handling upstream way instead
- Add 0042-UP-fix-signal-handling.patch
  * uxlsnr now handles all the signals sent to multipathd. This makes its
    signal handling posix compliant, and harder to mess up.
- Add 0043-RH-signal-waiter.patch
  * ioctl isn't a pthread cancellation point.  Send a signal to the waiter
    thread to break out of waiting in ioctl for a dm event.

* Fri May 17 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-51
- Add 0032-RHBZ-956464-mpathconf-defaults.patch
  * fix defaults listed in usage
- Add 0033-RHBZ-829963-e-series-conf.patch
- Add 0034-RHBZ-851416-mpathconf-display.patch
  * display whether or not multipathd is running in the status
- Add 0035-RHBZ-891921-list-mpp.patch
  * add a new path format wilcard to list the multipath device associated
    with a path
- Add 0036-RHBZ-949239-load-multipath-module.patch
  * load the dm-multipath kernel module when multipathd starts
- Add 0037-RHBZ-768873-fix-rename.patch
  * When deciding on a multipth devices name on reload, don't default to
    the existing name if there is no config file alias and user_friendly_names
    isn't set. Use the wwid.
- Modify multipath.conf
- Resolves: bz #768873, #950252

* Tue Apr 30 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-50
- Add 0031-RHBZ-957188-kpartx-use-dm-name.patch
  * use the basename of the devices that will be created to choose the
    delimiter instead of using the device name from the command line
- Resolves: bz #957188

* Fri Apr 26 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-49
- Modify 0020-RHBZ-907360-static-pthread-init.patch
  * Don't initialize uevent list twice
- Add 0029-RH-no-prio-put-msg.patch
- Add 0030-RHBZ-916528-override-queue-no-daemon.patch
  * Default to "queue_without_daemon no"
  * Add "forcequeueing daemon" and "restorequeueing daemon" cli commands
- Modify spec file to force queue_without_daemon when restarting
  multipathd on upgrades.

* Thu Apr  4 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-48
- Add 0026-fix-checker-time.patch
  * Once multipathd hit it max checker interval, it was reverting to
    to shortest checker interval
- Add 0027-RH-get-wwid.patch
  * Multipath wasn't correctly setting the multipath wwid when it read devices
    in from the kernel
- Add 0028-RHBZ-929078-refresh-udev-dev.patch
  * Make multipath try to get the UID of down devices.  Also, on ev_add_path,
    make multipathd reinitialize existing devices that weren't fully
    initialized before.

* Mon Apr  1 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-47
- Add 0021-RHBZ-919119-respect-kernel-cmdline.patch
  * keep the multipath.rules udev file from running and multipathd from
    starting if nompath is on the kernel command line
- Add 0022-RH-multipathd-check-wwids.patch
  * Whenever multipath runs configure, it will check the wwids, and
    add any missing ones to the wwids file
- Add 0023-RH-multipath-wipe-wwid.patch
  * multipath's -w command will remove a wwid from the wwids file
- Add 0024-RH-multipath-wipe-wwids.patch
  * multipath's -W command will set reset the wwids file to just the current
    devices
- Add 0025-UPBZ-916668_add_maj_min.patch
- Resolves: bz #919119

* Thu Mar 28 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-46
- Add 0020-RHBZ-907360-static-pthread-init.patch
  * statically initialize the uevent pthread structures 

* Sat Mar  2 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-45
- Updated to latest upstrem 0.4.9 code: multipath-tools-130222
  (git commit id: 67b82ad6fe280caa1770025a6bb8110b633fa136)
- Refresh 0001-RH-dont_start_with_no_config.patch
- Modify 0002-RH-multipath.rules.patch
- Modify 0003-RH-Make-build-system-RH-Fedora-friendly.patch
- Refresh 0004-RH-multipathd-blacklist-all-by-default.patch
- Refresh 0005-RH-add-mpathconf.patch
- Refresh 0006-RH-add-find-multipaths.patch
- Add 0008-RH-revert-partition-changes.patch
- Rename 0008-RH-RHEL5-style-partitions.patch to
	 0009-RH-RHEL5-style-partitions.patch
- Rename 0009-RH-dont-remove-map-on-enomem.patch to
	 0010-RH-dont-remove-map-on-enomem.patch
- Rename 0010-RH-deprecate-uid-gid-mode.patch to
	 0011-RH-deprecate-uid-gid-mode.patch
- Rename 0013-RH-kpartx-msg.patch to 0012-RH-kpartx-msg.patch
- Rename 0035-RHBZ-883981-cleanup-rpmdiff-issues.patch to
         0013-RHBZ-883981-cleanup-rpmdiff-issues.patch
- Rename 0039-RH-handle-other-sector-sizes.patch to
	 0014-RH-handle-other-sector-sizes.patch
- Rename 0040-RH-fix-output-buffer.patch to 0015-RH-fix-output-buffer.patch
- Add 0016-RH-dont-print-ghost-messages.patch
- Add 0017-RH-fix-sigusr1.patch
  * Actually this fixes a number of issues related to signals
- Rename 0018-RH-remove-config-dups.patch to 0018-RH-fix-factorize.patch
  * just the part that isn't upstream
- Add 0019-RH-fix-sockets.patch
  * makes abstract multipathd a cli sockets use the correct name.
- Set find_multipaths in the default config

* Wed Feb 20 2013 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-44
- Add 0036-UP-fix-state-handling.patch
  * handle transport-offline and quiesce sysfs state
- Add 0037-UP-fix-params-size.patch
- Add 0038-RH-fix-multipath.rules.patch
  * make sure multipath's link priority gets increased
- Add 0039-RH-handle-other-sector-sizes.patch
  * allow gpt partitions on 4k sector size block devices.
- Add 0040-RH-fix-output-buffer.patch
  * fix multipath -ll for large configuration.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-42
- Add 0034-RHBZ-887737-check-for-null-key.patch
- Add 0035-RHBZ-883981-cleanup-rpmdiff-issues.patch
  * Compile multipathd with full RELRO and PIE and install to /usr

* Mon Dec 17 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-41
- Add 0033-RH-dont-disable-libdm-failback-for-sync-case.patch
  * make kpartx -s and multipath use libdm failback device creation, so
    that they work in environments without udev

* Fri Nov 30 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-40
- Add 0032-RH-make-path-fd-readonly.patch
  * revert change made when adding persistent reservations, so that path fds
    are again opened O_RDONLY

* Fri Nov 30 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-39
- Add 0031-RHBZ-882060-fix-null-strncmp.patch

* Fri Nov 30 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-38
- Add 0026-RH-fix-mpathpersist-fns.patch
- Add 0027-RH-default-partition-delimiters.patch
  * Only use the -p delimiter when the device name ends in a number
- Add 0028-RH-storagetek-config.patch
- Add 0029-RH-kpartx-retry.patch
  * retry delete on busy loop devices
- Add 0030-RH-early-blacklist.patch
  * multipath will now blacklist devices by device type and wwid in
    store_pathinfo, so that it doesn't do a bunch of unnecessary work
    on paths that it would only be removing later on.

* Sat Nov 03 2012 Peter Rajnoha <prajnoha@redhat.com> 0.4.9-37
- Install multipathd.service for sysinit.target instead of multi-user.target.

* Thu Nov 01 2012 Peter Rajnoha <prajnoha@redhat.com> 0.4.9-36
- Start multipathd.service systemd unit before LVM units.

* Wed Oct 24 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-35
- Add 0022-RHBZ-864368-disable-libdm-failback.patch
  * make kpartx and multiapthd disable libdm failback device creation
- Add 0023-RHBZ-866291-update-documentation.patch
- Resolves: bz #864368, #866291

* Tue Oct 23 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-34
- Add 0021-RH-fix-oom-adj.patch
  * don't use OOM_ADJUST_MIN unless you're sure it's defined

* Tue Oct 23 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-33
- Modify 0016-RH-retain_hwhandler.patch
  * Check the dm-multipath module version, and don't enable
    retain_attached_hw_handler if the kernel doesn't support it
- Add 0019-RH-detect-prio.patch
  * add detect_prio option, to make multipath check if the device
    supports the ALUA prio, before defaulting to the configured prio
- Remove 0017-RH-netapp_config.patch
- Add 0020-RH-netapp-config.patch
  * new netapp config that uses retain_attached_hw_handler and
    detect_prio to autoconfigure ALUA and non-ALUA devices.

* Tue Oct  2 2012 Benjamin Marzinski <bmarizns@redhat.com> 0.4.9-32
- Modified 0018-RH-remove-config-dups.patch
  * Made modified config remove original only if the vendor/product
    exactly match

* Thu Sep 27 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-31
- Add 0014-RH-dm_reassign.patch
  * Fix reassign_maps option
- Add 0015-RH-selector_change.patch
  * devices default to using service-time selector
- Add 0016-RH-retain_hwhandler.patch
  * add retain_attached_hw_handler option, to let multipath keep an
    already attached scsi device handler
- Add 0017-RH-netapp_config.patch
- Add 0018-RH-remove-config-dups.patch
  * Clean up duplicates in the devices and blacklist sections

* Wed Sep 05 2012 Václav Pavlín <vpavlin@redhat.com> - 0.4.9-30
- Scriptlets replaced with new systemd macros (#850088)

* Tue Aug 21 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-29
- Updated to latest upstrem 0.4.9 code: multipath-tools-120821.tgz
  (git commit id: 050b24b33d3c60e29f7820d2fb75e84a9edde528)
  * includes 0001-RH-remove_callout.patch, 0002-RH-add-wwids-file.patch,
    0003-RH-add-followover.patch, 0004-RH-fix-cciss-names.patch
- Add 0013-RH-kpartx-msg.patch
- Modify 0002-RH-multipath.rules.patch
  * removed socket call from rules file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-27
- Updated to latest upstream 0.4.9 code : multipath-tools-120613.tgz
  (git commit id: cb0f7127ba90ab5e8e71fc534a0a16cdbe96a88f)
- Add 0001-RH-remove_callout.patch
  * multipath no longer uses the getuid callout.  It now gets the
    wwid from the udev database or the environment variables
- Add 0004-RH-fix-cciss-names.patch
  * convert cciss device names from cciss/cXdY to sysfs style cciss!cXdY
- Split 0009-RH-add-find-multipaths.patch into 0002-RH-add-wwids-file.patch
        and 0010-RH-add-find-multipaths.patch
- Add 0016-RH-change-configs.patch
  * default fast_io_fail to 5 and don't set the path selector in the
    builtin configs.
Resolves: bz #831978


* Thu May 17 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-26
- Add 0025-RHBZ-822714-update-nodes.patch
- Resolves: bz #822714

* Mon Apr 30 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-25
- Modify 0024-RH-libudev-monitor.patch
- Resolves: bz #805493

* Mon Apr 30 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-24
- Add requirements on libudev to spec file
- Resolves: bz #805493

* Mon Apr 30 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-23
- Add 0024-RH-libudev-monitor.patch

* Fri Feb 10 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-22
- Add 0012-RH-update-on-show-topology.patch
- Add 0013-RH-manpage-update.patch
- Add 0014-RH-RHEL5-style-partitions.patch
- Add 0015-RH-add-followover.patch
- Add 0016-RH-dont-remove-map-on-enomem.patch
- Add 0017-RH-fix-shutdown-crash.patch
- Add 0018-RH-warn-on-bad-dev-loss-tmo.patch
- Add 0019-RH-deprecate-uid-gid-mode.patch
- Add 0020-RH-dont-remove-map-twice.patch
- Add 0021-RH-validate-guid-partitions.patch
- Add 0022-RH-adjust-messages.patch
- Add 0023-RH-manpage-update.patch

* Tue Jan 24 2012 Benjamin Marzinski <bmarzins@redhat.com> 0.4.9-21
- Updated to latest upstream 0.4.9 code : multipath-tools-120123.tgz
  (git commit id: 63704387009443bdb37d9deaaafa9ab121d45bfb)
- Add 0001-RH-fix-async-tur.patch
- Add 0002-RH-dont_start_with_no_config.patch
- Add 0003-RH-multipath.rules.patch
- Add 0004-RH-update-init-script.patch
- Add 0005-RH-cciss_id.patch
- Add 0006-RH-Make-build-system-RH-Fedora-friendly.patch
- Add 0007-RH-multipathd-blacklist-all-by-default.patch
- Add 0008-RH-add-mpathconf.patch
- Add 0009-RH-add-find-multipaths.patch
- Add 0010-RH-check-if-multipath-owns-path.patch
- Add 0011-RH-add-hp_tur-checker.patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-19
- Modify 0103-add-disable-sync-option.patch
- Add 0104-RHBZ-737989-systemd-unit-fix.patch
  * systemd will only start multipathd if /etc/multipath.conf exists
- Add 0105-fix-oom-adj.patch
  * first try setting oom_score_adj

* Mon Aug 15 2011 Kalev Lember <kalevlember@gmail.com> - 0.4.9-18
- Rebuilt for rpm bug #728707

* Tue Jul 19 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-17
- Add 0103-add-disable-sync-option.patch
  * add a -n (nosync) option to multipath. This disables synchronous
    file creation with udev. 

* Fri Jul 15 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-16
- Modify 0012-RH-udev-sync-support.patch
- Modify 0021-RHBZ-548874-add-find-multipaths.patch
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
- Add 0025-RHBZ-508827-update-multipathd-manpage.patch through
      0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
  * sync with current state of RHEL6. Next release should include a updated
    source tarball with most of these fixes rolled in.
- Add 0102-RHBZ-690828-systemd-unit-file.patch
  * Add Jóhann B. Guðmundsson's unit file for systemd.
  * Add sub-package sysvinit for SysV init script.
- Resolves: bz #690828

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-14
- Modify 0021-RHBZ-548874-add-find-multipaths.patch
  * fix bug where mpathconf wouldn't create a multpath.conf file unless one
    already existed.

* Tue Feb 16 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-13
- Replace 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch
  with 0012-RH-udev-sync-support.patch
  * Add udev sync support to kpartx and multipath. In kpartx it is disabled
    unless you use the -s option.
- Refresh 0013-RH-add-weighted_prio-prioritizer.patch
- Refresh 0021-RHBZ-548874-add-find-multipaths.patch
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * kpartx now creates a 2 sector large device for dos extended
    partitions, just like the kernel does on the regular block devices.
- Add 0023-RHBZ-557810-emc-invista-config.patch
- Add 0024-RHBZ-565933-checker-timeout.patch
  * Multipath has a new option checker_timeout. If this is not set, 
    all path checker functions with explicit timeouts use
    /sys/block/sd<x>/device/timeout. If this is set, they use it instead.

* Fri Jan 22 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-12
- Refresh 0001-RH-queue-without-daemon.patch
- Refresh 0002-RH-path-checker.patch
- Modify 0010-RH-multipath-rules-udev-changes.patch
  * Fix udev rules to use DM_SBIN_PATH when calling kpartx
  * install udev rules to /lib/udev/rules.d instead of /etc/udev/rules.d
- Modify 0014-RH-add-hp_tur-checker.patch
- Add 0003-for-upstream-default-configs.patch
- Add 0016-RHBZ-554561-fix-init-error-msg.patch
- Add 0017-RHBZ-554592-man-page-note.patch
- Add 0018-RHBZ-554596-SUN-6540-config.patch
- Add 0019-RHBZ-554598-fix-multipath-locking.patch
- Add 0020-RHBZ-554605-fix-manual-failover.patch
- Add 0021-RHBZ-548874-add-find-multipaths.patch
  * Added find_multipaths multipath.conf option
  * Added /sbin/mpathconf for simple editting of multipath.conf
- Add 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * Make kpartx deal with logical partitions like it did in RHEL5.
    Don't create a dm-device for the extended partition itself.
    Create the logical partitions on top of the dm-device for the whole disk.

* Mon Nov 16 2009 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-11
- Add 0002-for-upstream-add-tmo-config-options.patch
  * Add fail_io_fail_tmo and dev_loss_tmo multipath.conf options
- Add 0013-RH-add-weighted_prio-prioritizer.patch
- Add 0014-RH-add-hp_tur-checker.patch
- Add 0015-RH-add-multipathd-count-paths-cmd.patch
- rename multipath.conf.redhat to multipath.conf, and remove the default
  blacklist.

* Tue Oct 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-10
- Updated to latest upstream 0.4.9 code : multipath-tools-091027.tar.gz
  (git commit id: a946bd4e2a529e5fba9c9547d03d3f91806618a3)
- Drop unrequired for-upstream patches.
- BuildRequires and Requires new device-mapper version for udev sync support.

* Tue Oct 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-9
- 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch

* Mon Oct 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-8
- Split patches in "for-upstream" and "RH" series.
- Replace 0011-RH-multipathd-blacklist-all-by-default.patch with
  version from Benjamin Marzinski.
- Update udev rules 0010-RH-multipath-rules-udev-changes.patch.
- rpmlint cleanup:
  * Drop useless-provides kpartx.
  * Cleanup tab vs spaces usage.
  * Summary not capitalized.
  * Missing docs in libs package.
  * Fix init script LSB headers.
- Drop README* files from doc sections (they are empty).

* Thu Oct 15 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-7
- Add patch 0010-RH-Set-friendly-defaults.patch:
  * set rcdir to fedora default.
  * do not install kpartx udev bits.
  * install redhat init script.
  * Cleanup spec file install target.
- Add patch 0011-RH-multipathd-blacklist-all-by-default.patch:
  * Fix BZ#528059
  * Stop installing default config in /etc and move it to the doc dir.

* Tue Oct 13 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-6
- Updated to latest upstream 0.4.9 code : multipath-tools-091013.tar.gz
  (git commit id: aa0a885e1f19359c41b63151bfcface38ccca176)
- Drop, now upstream, patches:
  * fix_missed_uevs.patch.
  * log_all_messages.patch.
  * uninstall.patch.
  * select_lib.patch.
  * directio_message_cleanup.patch.
  * stop_warnings.patch.
- Drop redhatification.patch in favour of spec file hacks.
- Drop mpath_wait.patch: no longer required.
- Merge multipath_rules.patch and udev_change.patch.
- Rename all patches based on source.
- Add patch 0009-RH-fix-hp-sw-hardware-table-entries.patch to fix
  default entry for hp_sw and match current kernel.
- Add multipath.conf.redhat as source instead of patch.
- spec file:
  * divide runtime and build/setup bits.
  * update BuildRoot.
  * update install section to apply all the little hacks here and there,
    in favour of patches against upstream.
  * move ldconfig invokation to libs package where it belong.
  * fix libs package directory ownership and files.

* Thu Aug 20 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-5
- Fixed problem where maps were being added and then removed.
- Changed the udev rules to fix some issues.

* Thu Jul 30 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-4
- Fixed build issue on i686 machines.

* Wed Jul 29 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-3
- Updated to latest upstream 0.4.9 code : multipath-tools-090729.tgz
  (git commit id: d678c139719d5631194b50e49f16ca97162ecd0f)
- moved multipath bindings file from /var/lib/multipath to /etc/multipath
- Fixed 354961, 432520

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 6 2009 Mike Snitzer <snitzer@redhat.com> - 0.4.9-1
- Updated to latest upstream 0.4.9 code: multipath-tools-090429.tgz
  (git commit id: 7395bcda3a218df2eab1617df54628af0dc3456e)
- split the multipath libs out to a device-mapper-multipath-libs package
- if appropriate, install multipath libs in /lib64 and /lib64/multipath

* Tue Apr 7 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-10
- Fix insecure permissions on multipathd.sock (CVE-2009-0115)

* Fri Mar 6 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-9
- Fix kpartx extended partition handling (475283)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 26 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-7
- Since libaio is now in /lib, not /usr/lib, multipath no longer needs to
  statically link against it. Fixed an error with binding file and WWIDs
  that include spaces. Cleaned up the messages from the directio checker
  function.  Fixed the udev rules. Fixed a regression in multipath.conf
  parsing
- Fixed 457530, 457589

* Wed Aug 20 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-6
- Updated to latest upstream 0.4.8 code: multipath-tools-080804.tgz
  (git commit id: eb87cbd0df8adf61d1c74c025f7326d833350f78)
- fixed 451817, 456397 (scsi_id_change.patch), 457530 (config_space_fix.patch)
  457589 (static_libaio.patch)

* Fri Jun 13 2008 Alasdair Kergon <agk@redhat.com> - 0.4.8-5
- Rebuild (rogue vendor tag). (451292)

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-4
- Fixed Makefile issues.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-3
- Fixed ownership build error.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-2
- Forgot to commit some patches.

* Mon May 19 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-1
- Updated to latest Upstream 0.4.8 code: multipath-tools-080519.tgz
  (git commit id: 42704728855376d2f7da2de1967d7bc71bc54a2f)

* Tue May 06 2008 Alasdair Kergon <agk@redhat.com> - 0.4.7-15
- Remove unnecessary multipath & kpartx static binaries. (bz 234928)

* Fri Feb 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7-14
- fix sparc64
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.7-13
- Autorebuild for GCC 4.3

* Wed Nov 14 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-12
- Fixed the dist tag so building will work properly.

* Mon Feb 05 2007 Alasdair Kergon <agk@redhat.com> - 0.4.7-11.fc7
- Add build dependency on new device-mapper-devel package.
- Add dependency on device-mapper.

* Wed Jan 31 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-10.fc7
- Update BuildRoot and PreReq lines.

* Mon Jan 15 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-9.fc7
- Fixed spec file.

* Mon Jan 15 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-8.fc7
- Update to latest code (t0_4_7_head2)

* Wed Dec 13 2006 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-7.fc7
- Update to latest code (t0_4_7_head1)

* Thu Sep  7 2006 Peter Jones <pjones@redhat.com> - 0.4.7-5
- Fix kpartx to handle with drives >2TB correctly.

* Thu Aug 31 2006 Peter Jones <pjones@redhat.com> - 0.4.7-4.1
- Split kpartx out into its own package so dmraid can use it without
  installing multipathd
- Fix a segfault in kpartx

* Mon Jul 17 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-4.0
- Updated to latest source. Fixes bug in default multipath.conf

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.1
- Added ncurses-devel to BuildRequires

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.0
- Updated to latest source. deals with change in libsysfs API

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.4.7-2.2.1
- rebuild

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.2
- fix tagging issue.

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.1
- changed BuildRequires from sysfsutils-devel to libsysfs-devel

* Wed Jun 28 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.0
- Updated to latest upstream source, fixes kpartx udev rule issue

* Tue Jun 06 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-1.0
- Updated to Christophe's latest source

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-16.0
- Newer upstream source (t0_4_5_post59).

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-12.3
- BuildRequires: libsepol-devel, readline-devel

* Mon Feb 27 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.5-12.2
- Prereq: chkconfig

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 0.4.5-12.1
- BuildRequires: libselinux-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-12.0.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Benjamin Marzinski <bmarzins@redhat.com> -0.4.5-12.0
- Updated to latest upstream source (t0_4_5_post56)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-9.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 19 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.1
- added patch for fedora changes

* Fri Dec 16 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.0
- Updated to latest upstream source (t)_4_5_post52)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec  4 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.6
- rebuild for newer libs

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.5
- unsplit kpartx.  parted knows how to do this now, so we don't
  need this in a separate package.

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.4
- split kpartx out into its own package

* Fri May 06 2005 Bill Nottingham <notting@redhat.com> - 0.4.4-2.3
- Fix last fix.

* Thu May 05 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.2
- Fix last fix.

* Wed May 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.1
- By default, disable the multipathd service.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.0
- Fix core dump from last build.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-1.0
- Move cache file into /var/cache/multipath.

* Fri Apr 08 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.1
- Remove pp_balance_units.

* Mon Apr 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.0
- Incorporate numerous upstream fixes.
- Update init script to distribution standards.

* Tue Mar 01 2005 Alasdair Kergon <agk@redhat.com> - 0.4.2-1.0
- Initial import based on Christophe Varoqui's spec file.
