package main

import (
	"fmt"
	"testing"
)

type Node struct {
	key, value int
	next, prev *Node
}

type LRUCache struct {
	capacity int
	head     *Node
	tail     *Node
	cache    map[int]*Node
}

func Constructor(capacity int) LRUCache {
	head := &Node{}
	tail := &Node{}
	head.next = tail
	tail.prev = head
	return LRUCache{
		capacity: capacity,
		head:     head,
		tail:     tail,
		cache:    make(map[int]*Node),
	}
}

func (this *LRUCache) remove(node *Node) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (this *LRUCache) insert(node *Node) {
	head := this.head
	head.next.prev = node
	node.next = head.next
	head.next = node
	node.prev = head
}

func (this *LRUCache) Get(key int) int {
	if node, exists := this.cache[key]; exists {
		this.remove(node)
		this.insert(node)
		return node.value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, exists := this.cache[key]; exists {
		this.remove(node)
		this.insert(node)
		node.value = value
		return
	}
	fmt.Println(len(this.cache), this.capacity)
	if len(this.cache) == this.capacity {
		lru := this.tail.prev
		this.remove(lru)
		delete(this.cache, lru.key)
	}
	node := &Node{key: key, value: value}
	this.insert(node)
	this.cache[key] = node
}

func TestLRU(t *testing.T) {
	capacity := 2
	obj := Constructor(capacity)
	obj.Put(1, 2)
	obj.Put(2, 3)
	obj.Get(1)
	obj.Get(2)
	obj.Put(3, 4)
	fmt.Println(obj.cache)
}
