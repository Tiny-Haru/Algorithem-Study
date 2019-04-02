package main

import "fmt"

type Node struct {
	Value int
}

func (n *Node) String() string {
	return fmt.Sprint(n.Value)
}

func NewStack() *Stack {
	return &Stack{}
}

type Stack struct {
	nodes []*Node
	count int
}

func (s *Stack) Push(n *Node) {
	s.nodes = append(s.nodes[:s.count], n)
	s.count++
}

func (s *Stack) Pop() *Node {
	if s.count == 0 {
		return nil
	}
	s.count--
	return s.nodes[s.count]
}

func main() {
	s := NewStack()
	r := s

	n := 0
	fmt.Scanln(&n)
	command := ""
	a := 0

	for i := 0; i < n; i++ {
		fmt.Scanln(&command)

		if command == "push"{
			fmt.Scanln(&a)
			s.Push(&Node{a})
			r.Push(&Node{a})
		} else if command == "pop" {
			if r.Pop() == nil {
				fmt.Println("-1")
			} else {
				fmt.Println(s.Pop())
			}
		} else if command == "size" {
			fmt.Println(s.count)
		} else if command == "empty" {
			if r.Pop() == nil {
				fmt.Println("1")
			} else {
				fmt.Println("0")
			}
		} else if command == "top" {
			fmt.Println("top")

		}
	}
}
