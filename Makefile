generate-client:
	@echo "🔄 Generating API client from OpenAPI spec..."
	openapi-generator-cli generate -i common_v1.yaml -g python -c openapi-config.yaml
	@echo "✅ API client generated successfully"