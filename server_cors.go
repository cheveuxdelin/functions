package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
    "math/rand"
	"github.com/gin-contrib/cors"
)

func main() {

	r := gin.Default()
	r.Use(cors.Default())

	fmt.Println("MO")

	var db []string

	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, db[rand.Intn(len(db))] )
	})

	r.GET("/all", func(c *gin.Context) {
		c.JSON(http.StatusOK, db)
	})

	r.POST("/", func(c *gin.Context) {
		data, err := c.GetRawData()

		if err == nil {
			db = append(db, string(data))
			c.String(http.StatusOK, "uwu")
		}
	})

	r.Run(":8080")
}
