Just a log implementation

Implements a Logger type


Logger methods:
 - Default - constructor
 - New(out i.o, prefix, flag) - advanced constructor
 - Fatal - logs on fatal level and call os.Exit(1)
 - Fatalf - fatal + printf
 - Fatalln - fatal + println
 - Flags - returns output flags ( The flag bits are Ldate, Ltime, and so on.)
 - Output - Output writes the output for a logging event. The string s contains the text to print after the prefix specified by the flags of the Logger.
 - Panic - Print + panic
 - Panicln, Panicf - same as in Fatalf, Fatalln
 - Prefix - returns prefix
 - Print - prints to logger
 - Prints, Println - same as Fatalf, Fatalln
 - SetFlags, SetOutput, SetPrefix
 - Writer - returns writer