.PHONY: help install run test clean format lint docker-build docker-run stop

help:
	@echo "LAN File Share - Makefile Commands"
	@echo "===================================="
	@echo ""
	@echo "Development:"
	@echo "  make install        - Install dependencies"
	@echo "  make run            - Run the application"
	@echo "  make test           - Run unit tests"
	@echo "  make coverage       - Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format         - Format code with black"
	@echo "  make lint           - Lint code with flake8"
	@echo "  make style-check    - Check code style"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean          - Remove Python cache files"
	@echo "  make clean-all      - Remove all generated files"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   - Build Docker image"
	@echo "  make docker-run     - Run in Docker container"
	@echo "  make docker-stop    - Stop Docker container"
	@echo ""

install:
	@echo "Installing dependencies..."
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

install-dev:
	@echo "Installing development dependencies..."
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements-dev.txt
	@echo "✅ Development dependencies installed!"

run:
	@echo "Starting LAN File Share..."
	python3 app.py

test:
	@echo "Running tests..."
	python3 -m pytest test_app.py -v

coverage:
	@echo "Running tests with coverage..."
	python3 -m pytest test_app.py --cov=. --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/index.html"

format:
	@echo "Formatting code with black..."
	python3 -m black app.py config.py test_app.py
	@echo "✅ Code formatted!"

lint:
	@echo "Linting code with flake8..."
	python3 -m flake8 app.py config.py test_app.py

style-check: lint
	@echo "✅ Style check complete!"

clean:
	@echo "Cleaning Python cache files..."
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	@echo "✅ Cleaned!"

clean-all: clean
	@echo "Removing virtual environment and test files..."
	rm -rf venv/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	@echo "✅ All cleaned!"

docker-build:
	@echo "Building Docker image..."
	docker build -t lan-file-share .
	@echo "✅ Docker image built!"

docker-run: docker-build
	@echo "Starting Docker container..."
	docker run -p 5000:5000 -v shared_files:/app/shared_files lan-file-share

docker-stop:
	@echo "Stopping Docker container..."
	docker stop lan-file-share 2>/dev/null || echo "Container not running"
	@echo "✅ Container stopped!"

docker-compose-up:
	@echo "Starting with Docker Compose..."
	docker-compose up -d
	@echo "✅ Services started!"

docker-compose-down:
	@echo "Stopping Docker Compose services..."
	docker-compose down
	@echo "✅ Services stopped!"

requirements-update:
	@echo "Updating requirements.txt..."
	pip freeze > requirements.txt
	@echo "✅ requirements.txt updated!"

# Development workflow shortcuts
dev-setup: install-dev lint format
	@echo "✅ Development environment ready!"

dev-check: lint test
	@echo "✅ All checks passed!"

all: clean install test
	@echo "✅ Full build and test complete!"
