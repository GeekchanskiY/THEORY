

[[React WebPack]]


## Hooks
_Hooks_ are a new addition in React 16.8. They let you use state and other React features without writing a class.

### Use State

```jsx
import React, { useState } from 'react';

function Example() {
  // Declare a new state variable, which we'll call "count"  const [count, setCount] = useState(0);
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### Use Effect
The _Effect Hook_ lets you perform side effects in function components:
```jsx
import React, { useState, useEffect } from 'react';
function Example() {
  const [count, setCount] = useState(0);

  // Similar to componentDidMount and componentDidUpdate:  useEffect(() => {    // Update the document title using the browser API    document.title = `You clicked ${count} times`;  });
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

It can be used with cleanup by adding:
```jsx
return function cleanup() {      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);    };
```
Inside of the use effect anonymous function. In a React class, you would typically set up a subscription in `componentDidMount`, and clean it up in `componentWillUnmount`.

Tip: optimizing performance:
In some cases, cleaning up or applying the effect after every render might create a performance problem. In class components, we can solve this by writing an extra comparison with `prevProps` or `prevState` inside `componentDidUpdate`:

```jsx
componentDidUpdate(prevProps, prevState) {
  if (prevState.count !== this.state.count) {
    document.title = `You clicked ${this.state.count} times`;
  }
}
```

This requirement is common enough that it is built into the `useEffect` Hook API. You can tell React to _skip_ applying an effect if certain values haven’t changed between re-renders. To do so, pass an array as an optional second argument to `useEffect`:

```jsx
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]); // Only re-run the effect if count changes
```

This also works for effects that have a cleanup phase:

```jsx
useEffect(() => {
  function handleStatusChange(status) {
    setIsOnline(status.isOnline);
  }

  ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
  return () => {
    ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
  };
}, [props.friend.id]); // Only re-subscribe if props.friend.id changes
```

### Use Memo
`useMemo` is a React Hook that lets you cache the result of a calculation between re-renders.

```jsx
const cachedValue = useMemo(calculateValue, dependencies)

```

### Use Reducer
`useReducer` is a React Hook that lets you add a [reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer) to your component.

```jsx
const [state, dispatch] = useReducer(reducer, initialArg, init?)
```
### Custom hooks:
**A custom Hook is a JavaScript function whose name starts with ”`use`” and that may call other Hooks.** For example, `useFriendStatus` below is our first custom Hook:

```jsx
import { useState, useEffect } from 'react';

function useFriendStatus(friendID) {  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }

    ChatAPI.subscribeToFriendStatus(friendID, handleStatusChange);
    return () => {
      ChatAPI.unsubscribeFromFriendStatus(friendID, handleStatusChange);
    };
  });

  return isOnline;
}
```

Now that we’ve extracted this logic to a `useFriendStatus` hook, we can _just use it:_

```jsx
function FriendStatus(props) {
  const isOnline = useFriendStatus(props.friend.id);
  if (isOnline === null) {
    return 'Loading...';
  }
  return isOnline ? 'Online' : 'Offline';
}
```

## HOCs

A higher-order component (HOC) is an advanced technique in React for reusing component logic. HOCs are not part of the React API, per se. They are a pattern that emerges from React’s compositional nature.

Concretely, **a higher-order component is a function that takes a component and returns a new component.**

```jsx
const EnhancedComponent = higherOrderComponent(WrappedComponent);
```