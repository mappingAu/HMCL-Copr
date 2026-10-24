# Local build helpers for the HMCL RPM.
#
#   make srpm   build out/*.src.rpm
#   make rpm    build out/noarch/*.rpm (SRPM + RPM)
#   make fetch  only download the release jar
#   make clean  remove build artefacts
#
# The version is read from hmcl.spec; nothing else has to be kept in sync.

NAME    := hmcl
VERSION := $(shell sed -n 's/^Version:[[:space:]]*//p' $(NAME).spec | head -n 1)
TOP     := $(CURDIR)
OUT     := $(TOP)/out
TOPDIR  := $(OUT)/rpmbuild

RPMBUILD_FLAGS := \
	--define "_topdir $(TOPDIR)" \
	--define "_sourcedir $(TOP)" \
	--define "_srcrpmdir $(OUT)" \
	--define "_rpmdir $(OUT)"

.PHONY: all fetch srpm rpm clean
.DEFAULT_GOAL := rpm

all: rpm

## Download the prebuilt jar referenced by Source0.
fetch:
	spectool -g --define "_sourcedir $(TOP)" $(NAME).spec

srpm: fetch
	@mkdir -p $(TOPDIR) $(OUT)
	rpmbuild -bs $(RPMBUILD_FLAGS) $(NAME).spec

rpm: fetch
	@mkdir -p $(TOPDIR) $(OUT)
	rpmbuild -ba $(RPMBUILD_FLAGS) $(NAME).spec

clean:
	rm -rf $(OUT) $(NAME)-*.tar.gz $(NAME)-*.jar
