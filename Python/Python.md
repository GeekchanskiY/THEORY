[[Python frameworks & Libs]]


### Python + Obsidian example
(To have a better experience install 'Execute code' plugin: https://github.com/twibiral/obsidian-execute-code)

```python {pre}
import random
```

```run-python
def magic_commands() -> None:
	print("Vault path:", @vault_path)
	print("Vault url:", @vault_url)
	
	print("Note path:", @note_path)
	print("Note url:", @note_url)
	
	print("Note title:", @title)	
	#@show("image.png")
	#@show("image.png", 100, 100)
	#@show("https://upload.wikimedia.org/wikipedia/commons/d/de/TestScreen_square.svg", 10%, 10%, "center")
	@html("<h1>HTML Caption</h1>")
	@html('''
	<svg width="100%" height="100%" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
	  <circle cx="300" cy="300" r="250" style="fill:peru;" />
	  <circle cx="200" cy="250" r="50" style="fill:black;" />
	  <circle cx="400" cy="250" r="50" style="fill:black;" />
	  <circle cx="190" cy="230" r="20" style="fill:white;" />
	  <circle cx="390" cy="230" r="20" style="fill:white;" />
	  <circle cx="250" cy="400" r="85" style="fill:saddlebrown;" />
	  <circle cx="350" cy="400" r="85" style="fill:saddlebrown;" />
	  <ellipse cx="300" cy="380" rx="50" ry="35" style="fill:black;" />
	  <ellipse cx="130" cy="100" rx="110" ry="70" style="fill:saddlebrown;"/>
	<ellipse cx="470" cy="100" rx="110" ry="70" style="fill:saddlebrown;" />
	</svg> 
	''')	

if __name__ == '__main__':
	print('hello, OBSIDIAN!')
	print(f'Today\'s number is: {random.randint(1, 100)}')
	magic_commands()
	
```

```python {post}
print('see you later!')
```