## Constants
```go
const (
	Layout      = "01/02 03:04:05PM '06 -0700" // The reference time, in numerical order.
	ANSIC       = "Mon Jan _2 15:04:05 2006"
	UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
	RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
	RFC822      = "02 Jan 06 15:04 MST"
	RFC822Z     = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone
	RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
	RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
	RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone
	RFC3339     = "2006-01-02T15:04:05Z07:00"
	RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
	Kitchen     = "3:04PM"
	// Handy time stamps.
	Stamp      = "Jan _2 15:04:05"
	StampMilli = "Jan _2 15:04:05.000"
	StampMicro = "Jan _2 15:04:05.000000"
	StampNano  = "Jan _2 15:04:05.000000000"
	DateTime   = "2006-01-02 15:04:05"
	DateOnly   = "2006-01-02"
	TimeOnly   = "15:04:05"
)
```

### Default behavior
By default, if you have `time.Time` in your struct which you wish to unmarshal from json, it supports `RFC 3339` format.

## Types
### Timer
```go
type Timer struct {
	C <-chan [Time](https://pkg.go.dev/time#Time)
	// contains filtered or unexported fields
}
```

Timer resolution varies depending on the Go runtime, the operating system and the underlying hardware. On Unix, the resolution is ~1ms. On Windows version 1803 and newer, the resolution is ~0.5ms. On older Windows versions, the default resolution is ~16ms, but a higher resolution may be requested using [golang.org/x/sys/windows.TimeBeginPeriod](https://pkg.go.dev/golang.org/x/sys/windows#TimeBeginPeriod).

```go
func AfterFunc(d Duration, f func()) *Timer
```
`AfterFunc` waits for the `Duration` to elapse and then calls f in its own goroutine. It returns a Timer that can be used to cancel the call using its Stop method. The returned Timer's C field is not used and will be nil.

```go
func NewTimer(d Duration) *Timer
```
`NewTimer` creates a new `Timer` that will send the current time on its channel after at least duration d.

Before Go 1.23, the garbage collector did not recover timers that had not yet expired or been stopped, so code often immediately deferred t.Stop after calling `NewTimer`, to make the timer recoverable when it was no longer needed. As of Go 1.23, the garbage collector can recover unreferenced timers, even if they haven't expired or been stopped. The Stop method is no longer necessary to help the garbage collector. (Code may of course still want to call Stop to stop the timer for other reasons.)

Before Go 1.23, the channel associated with a Timer was asynchronous (buffered, capacity 1), which meant that stale time values could be received even after Timer.Stop or Timer.Reset returned. As of Go 1.23, the channel is synchronous (unbuffered, capacity 0), eliminating the possibility of those stale values.

The `GODEBUG` setting `asynctimerchan=1` restores both pre-Go 1.23 behaviors: when set, unexpired timers won't be garbage collected, and channels will have buffered capacity. This setting may be removed in Go 1.27 or later.

#### Methods
```go
func (t *Timer) Stop() bool
```
`Stop` prevents the `Timer` from firing. It returns true if the call stops the timer, false if the timer has already expired or been stopped.

```go
func (t *Timer) Reset(d Duration) bool
```
Reset changes the timer to expire after duration d. It returns true if the timer had been active, false if the timer had expired or been stopped. If it's called to `AfterFunc` `Timer`, `Reset` either reschedules when f will run, in which case `Reset` returns `true`, or schedules `f` to run again, in which case it returns `false`.

### Weekday
A Weekday specifies a day of the week (Sunday = 0, ...).
```go
type Weekday int

const (
	Sunday Weekday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
)
```
#### Methods
```go
func (d Weekday) String() string
```
String returns the English name of the day ("Sunday", "Monday", ...).

### Time
```go
type Time struct {
	// contains filtered or unexported fields
}
```
A Time represents an instant in time with nanosecond precision.

Programs using times should typically store and pass them as values, not pointers. That is, time variables and struct fields should be of type `time.Time`, not `*time.Time`.

The zero value of type Time is January 1, year 1, 00:00:00.000000000 UTC. As this time is unlikely to come up in practice, the `Time.IsZero` method gives a simple way of detecting a time that has not been initialized explicitly.

Each `Time` has a specified `Location`. The methods `Time.Local`, `Time.UTC` and `Time.In` return a `Time` with a specific Location. Changing the Location of Time value with these methods does not change the actual instant it represents. only the time zone in which to interpret it.

Note that the Go == operator compares not just the time instant but also the Location and the monotonic clock reading. Therefore, Time values should not be used as map or database keys without first guaranteeing that the identical Location has been set for all values, which can be achieved through use of the UTC or Local method, and that the monotonic clock reading has been stripped by setting t = t.Round(0). In general, prefer t.Equal(u) to t == u, since t.Equal uses the most accurate comparison available and correctly handles the case when only one of its arguments has a monotonic clock reading.

#### Methods

```go
func Now() Time
```
returns current local time

```go
func Date(year int, month Month, day, hour, min, sec, nsec int, loc *Location) Time
```
returns input time. Values may be outside the usual ranges, and converts it appropriately. For example, October 32 will be converted to November 1.

```go
func Parse(layout, value string) (Time, error)
```
parses time from string. 
For layouts specifying the two-digit year 06, a value NN >= 69 will be treated as 19NN and a value NN < 69 will be treated as 20NN.

```go
func ParseInLocation(lauout, value string, loc *Location) (Time, error)
```
`ParseInLocation` is like `Parse` but differs in two important ways. First, in the absence of time zone information, Parse interprets a time as UTC; `ParseInLocation` interprets the time as in the given `Location`. Second, when given a zone offset or abbreviation, Parse tries to match it against the Local location; `ParseInLocation` uses the given location.

```go
func Unix(sec, nsec int64) Time
```
`Unix` returns the local `Time` corresponding to the given Unix time.

```go
func UnixMicro(usec int64) Time
```
`UnixMicro` returns the local `Time` corresponding to the given Unix time, `usec` microseconds since January 1, 1970 UTC.

```go
func UnixMilli(msec int64) Time
```
`UnixMilli` returns the local `Time` corresponding to the given Unix time,`msec` milliseconds since January 1, 1970 UTC.

```go
func (t Time) Add(d Duration) Time
```
`Add` returns the time + d

```go
func (t Time) Sub(u time) Duration
```
Sub returns the duration t-u. If the result exceeds the maximum (or minimum) value that can be stored in a `Duration`.

```go
func (t Time) Truncate(d Duration) Time
```
Truncate returns the result of rounding t down to a multiple of d (since the zero time). If d <= 0, Truncate returns t stripped of any monotonic clock reading but otherwise unchanged.

```go
func (t Time) AddDate(years, months, days int) Time
```
Same as `Add`. Input values may be negative.

```go
func (t Time) After(u Time) bool
func (t Time) Before(u Time) bool
```
returns bool if t is after/before u

```go
func (t Time) Format(layout string) string
func (t Time) AppendFormat(b []byte, layout string) string
```
`Format` formats the time like in the layout string, and returns a string representation.
`AppendFormat` is the same, but appends the textual representation to b and returns the extended buffer

```go
func (t Time) Clock() (hour, min, sec int)
func (t Time) Date() (year int, month Month, day int)
```
`Clock` and `Date` methods return values without including time for `Date`, and date for `Time`

```go
func (t Time) Compare(u Time) int
```
`Compare` compares t and u, and returns -1 if t is before u, if t is after u returns +1, or returns 0, if they are equal.

```go
func (t Time) Year() int
func (t Time) YearDay() int
func (t Time) Month() Month
func (t Time) Day() int
func (t Time) Hour() int
func (t Time) Minute() int
func (t Time) Second() int
func (t Time) NanoSecond() int
```
These `Time` methods return numeric values of given attributes.

```go
func (t Time) GoString() string
```
`GoString` returns source-code string value like `time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)`

```go
func (t *Time) GobDecode(data []byte) error
func (t Time) GobEncode() ([]byte, error)
```
`GobDecode` & `GobEncode` implements the `gob.GobDecoder` interface.

```go
func (t Time) In(loc *Location) Time
```
`In` represents time in given `Location`, panic if pointer is nil.

```go
func (t Time) ISOWeek() (year, week int)
```
`ISOWeek` returns the ISO 8601 year and week number in which t occurs. Week ranges from 1 to 53. Jan 01 to Jan 03 of year n might belong to week 52 or 53 of year n-1, and Dec 29 to Dec 31 might belong to week 1 of year n+1.

```go
func (t Time) IsDST() bool
```
`IsDST` reports whether the time in the configured location is in Daylight Savings Time.

```go
func (t Time) IsZero() bool
```
`IsZero` reports whether t represents the zero time instant, January 1, year 1, 00:00:00 UTC.

```go
func (t Time) Local() Time
```
Returns t with the `Location` set to local time.

```go
func (t Time) Location() *Location
```
Returns associated location if exists

```go
func (t Time) MarshalJSON() ([]byte, error)
func (t Time) MarshalText() ([]byte, error)
```
Implements `json.Marshaler` and `encoding.TextMarshaler` interface. The time is formatted in `RFC 3339` format with sub-second precision.

```go
func (t Time) Round(d Duration) Time

// Examples:
//
// t.Round(   1ms) = 12:15:30.918
// t.Round(    1s) = 12:15:31
// t.Round(    2s) = 12:15:30
// t.Round(  1m0s) = 12:16:00
// t.Round( 10m0s) = 12:20:00
// t.Round(1h0m0s) = 12:00:00
```
`Round` returns the result of rounding t to the nearest multiple of d (since the zero time). The rounding behavior for halfway values is to round up. If d <= 0, `Round` returns t stripped of any monotonic clock reading but otherwise unchanged.

```go
func (t Time) Zone() (name string, offset int)
func (t Time) ZoneBounds() (start, end Time)
```
`Zone` computes the time zone in effect at time t, returning the abbreviated name of the zone (such as `"CET"`) and its offset in seconds east of UTC.
`ZoneBounds` returns the bounds of the time zone in effect at time t. The zone begins at start and the next zone begins at end. If the zone begins at the beginning of time, start will be returned as a zero `Time`. If the zone goes on forever, end will be returned as a zero `Time`. The `Location` of the returned times will be the same as t.


### Duration
```go
type Duration int64
```
A Duration represents the elapsed time between two instants as an `int64` nanosecond count. The representation limits the largest representable duration to approximately 290 years.

#### Methods
```go
func ParseDuration(s string) (Duration, error)
```
`ParseDuration` parses a duration string. A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

```go
func Since(t Time) Duration
func Until(t Time) Duration
```
`Since` returns the time elapsed since t. It is shorthand for `time.Now().Sub(t)`.
`Until` returns the duration until t. It is shorthand for `t.Sub(time.Now())`.

```go
func (d Duration) Abs() Duration
```
`Abs` returns the absolute value of d

```go
func (d Duration) Hours() float64
func (d Duration) Microseconds() int64
func (d Duration) Milliseconds() int64
func (d Duration) Minutes() float64
func (d Duration) Seconds() float64
```
These methods represents values of duration in specified format

```go
func (d Duration) Round(m Duration) Duration
```
Rounds `Duration` in the same way as `func (t Time) Round(m Duration) Time`

```go
func (d Duration) String() string
```
String returns a string representing the duration in the form "72h3m0.5s". Leading zero units are omitted. As a special case, durations less than one second format use a smaller unit (milli-, micro-, or nanoseconds) to ensure that the leading digit is non-zero. The zero duration formats as 0s.

```go
func (d Duration) Truncate(m Duration) Duration
```
Truncate returns the result of rounding d toward zero to a multiple of m. If m <= 0, Truncate returns d unchanged.

### Location
```go
type Location struct {}
```
A Location maps time instants to the zone in use at that time. Typically, the Location represents the collection of time offsets in use in a geographical area. For many Locations the time offset varies depending on whether daylight savings time is in use at the time instant.

Location is used to provide a time zone in a printed Time value and for calculations involving intervals that may cross daylight savings time boundaries.
#### Methods
```go
func FixedZone(name string, offset int) *Location
```
`FixedZone` returns a `Location` that always uses the given zone name and offset (seconds east of UTC).

```go
func LoadLocation(name string) (*Location, error)
```
`LoadLocation` returns the Location with the given name if exists, else error.

```go
func LoadLocationFromTZData(name string, data []byte) (*Location, error)
```
`LoadLocationFromTZData` returns a Location with the given name initialized from the `IANA` Time Zone database-formatted data.

```go
func (l *Location) String() string
```
Returns string value of `Location`

### Ticker
```go
type Ticker struct {
	C <-chan Time
	// contains filtered or unexported fields
}
```
`NewTicker` returns a new Ticker containing a channel that will send the current time on the channel after each tick. The period of the ticks is specified by the duration argument. The ticker will adjust the time interval or drop ticks to make up for slow receivers. The duration d must be greater than zero; if not, `NewTicker` will `panic`.

#### Methods
```go
func (t *Ticker) Reset(d Duration)
func (t *Ticker) Stop()
```
`Reset` sets new ticking period, and `Stop` stops ticking