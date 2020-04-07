all:
	tarball

tarball:
	spectool -g gearman-plugin.spec

clean:
	git clean -fd

.PHONY: all tarball clean
