package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"time"
)

func fib(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return a
}

func fibHandler(w http.ResponseWriter, r *http.Request) {
	start := time.Now()

	// Extração otimizada do parâmetro
	n, err := strconv.Atoi(r.URL.Path[5:])
	if err != nil {
		http.Error(w, `{"error":"Invalid number"}`, http.StatusBadRequest)
		return
	}

	// Cálculo rápido
	result := fib(n)

	// Serialização direta
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"result":%d}`, result)

	log.Printf("n=%d | Go: %v", n, time.Since(start))
}

func main() {
	server := &http.Server{
		Addr:         ":8080",
		ReadTimeout:  1 * time.Second,
		WriteTimeout: 1 * time.Second,
		Handler:      http.HandlerFunc(fibHandler),
	}

	log.Println("Servidor Go otimizado iniciado")
	log.Fatal(server.ListenAndServe())
}
