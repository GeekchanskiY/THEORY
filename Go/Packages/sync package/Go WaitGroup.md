
```go
// bad example
func bad(urls []string){
	wg := &sync.WaitGroup()
	
	for _, url := range urls{
		go func(url string){
			wg.Add(1) // BAD
			defer wg.Done()
			
			fetch(url)
		}(url)
	}
	
	wg.Wait()
}

// good example
func bad(urls []string){
	wg := &sync.WaitGroup()
	
	// Alternative
	// wg.Add(len(urls))
	
	for _, url := range urls{
		wg.Add(1) // GOOD
		go func(url string){
			
			defer wg.Done()
			
			fetch(url)
		}(url)
	}
	
	wg.Wait()
}

// explanation:

// in first example, you can possibly call wg.Wait() before all wg.Add
// are called
```