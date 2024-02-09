

### Core components
<table style="font-size:12px;"><thead><tr><th>React Native UI Component</th><th>Android View</th><th>iOS View</th><th>Web Analog</th></tr></thead><tbody><tr><td><code>&lt;View&gt;</code></td><td><code>&lt;ViewGroup&gt;</code></td><td><code>&lt;UIView&gt;</code></td><td>A non-scrolling <code>&lt;div&gt;</code></td></tr><tr><td><code>&lt;Text&gt;</code></td><td><code>&lt;TextView&gt;</code></td><td><code>&lt;UITextView&gt;</code></td><td><code>&lt;p&gt;</code></td></tr><tr><td><code>&lt;Image&gt;</code></td><td><code>&lt;ImageView&gt;</code></td><td><code>&lt;UIImageView&gt;</code></td><td><code>&lt;img&gt;</code></td></tr><tr><td><code>&lt;ScrollView&gt;</code></td><td><code>&lt;ScrollView&gt;</code></td><td><code>&lt;UIScrollView&gt;</code></td><td><code>&lt;div&gt;</code></td></tr><tr><td><code>&lt;TextInput&gt;</code></td><td><code>&lt;EditText&gt;</code></td><td><code>&lt;UITextField&gt;</code></td><td><code>&lt;input type="text"&gt;</code></td></tr></tbody></table>

Basically, same as react, but some components have different names IMHO


### Platform-specific code
```jsx
import {Platform, StyleSheet} from 'react-native';  
  
const styles = StyleSheet.create({  
height: Platform.OS === 'ios' ? 200 : 100,  
});
```

Platform.OS may be: 'ios' | 'android' | 'native' | 'default'

Platform.Version

**platform-specific extensions**
BigButton.ios.js  
BigButton.android.js

```jsx
import BigButton from './BigButton';
// Selects for android/ios automatically!!!
```

Container.js # picked up by webpack, Rollup or any other Web bundler
Container.native.js # picked up by the React Native bundler for both Android and iOS (Metro)