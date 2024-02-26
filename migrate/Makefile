.PHONY: install migrate down drop

# Set default env as develop if ENV is not specified.
ENV ?= develop

-include .env.${ENV}.secret

MIGRATE := migrate -source file://ddl/postgresql -database 'postgres://$(CONNECTION_STRING)'

install:
	go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@v4.17.0

migrate:
	@echo "Migrating..."
	@if ! $(MIGRATE) up; then \
		echo "Error: Migration failed"; \
		exit 1; \
	fi
	@echo "Done!"

down:
	@echo "Migrating(down) DB.."
	@echo y | $(MIGRATE) down 1
	@echo "Done!"

drop:
	@echo "Dropping..."
	@if ! $(MIGRATE) down; then \
		echo "Error: Dropping migration failed"; \
		exit 1; \
	fi
	@echo "Done!"