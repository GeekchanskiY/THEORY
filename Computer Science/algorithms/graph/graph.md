In computer science, a **graph** is an abstract data type that is meant to implement the undirected graph") and directed graph concepts from the field of graph theory within mathematics.

A graph data structure consists of a finite (and possibly mutable) set") of _vertices_ (also called _nodes_ or _points_), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as _edges_ (also called _links_ or _lines_), and for a directed graph are also known as _edges_ but also sometimes _arrows_ or _arcs_. The vertices may be part of the graph structure, or may be external entities represented by integer indices or references").

A graph data structure may also associate to each edge some _edge value_, such as a symbolic label or a numeric attribute (cost, capacity, length, etc.).

The basic operations provided by a graph data structure _G_ usually include:

- adjacent(_G_, _x_, _y_): tests whether there is an edge from the vertex _x_ to the vertex _y_;
- neighbors(_G_, _x_): lists all vertices _y_ such that there is an edge from the vertex _x_ to the vertex _y_;
- add_vertex(_G_, _x_): adds the vertex _x_, if it is not there;
- remove_vertex(_G_, _x_): removes the vertex _x_, if it is there;
- add_edge(_G_, _x_, _y_, _z_): adds the edge _z_ from the vertex _x_ to the vertex _y_, if it is not there;
- remove_edge(_G_, _x_, _y_): removes the edge from the vertex _x_ to the vertex _y_, if it is there;
- get_vertex_value(_G_, _x_): returns the value associated with the vertex _x_;
- set_vertex_value(_G_, _x_, _v_): sets the value associated with the vertex _x_ to _v_.

Structures that associate values to the edges usually also provide:

- get_edge_value(_G_, _x_, _y_): returns the value associated with the edge (_x_, _y_);
- set_edge_value(_G_, _x_, _y_, _v_): sets the value associated with the edge (_x_, _y_) to _v_.