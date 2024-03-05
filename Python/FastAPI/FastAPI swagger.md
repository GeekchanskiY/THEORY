
### Theme configuration
It can be achieved by directly changing ui parameters in fastapi startup
```python
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
```