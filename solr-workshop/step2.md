Let's explore some of the query capabilities of Solr. The most simple querying you will perform with Solr will be searching for _terms_ and _phrases_ in a particular _field_. 

Let's query the Solr `select` endpoint, passing in the query `q=manu:apple`. This tells Solr that we want to return any documents where the `manu` field contains the word `apple`. 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=manu:apple"`{{execute}}


We can tell Solr to return the results ordered by Price, with the highest price first. We do this by appending a `sort` operator: `sort=price%20desc`

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=name:video&sort=price%20desc"`{{execute}}


Great! But we're getting a lot of fields back which aren't needed. We can use the `fl=` query parameter to list only the fields we want: 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=*:*&fl=name,manu,price"`{{execute}}

Much easier to read. Notice that our results response includes a total number of matches found. `"response":{"numFound":32,"start":0,..` - but that only 10 results are listed out on screen. Our Solr core has `10` as the default _page size_. We can control this by passing in the `rows` and `starts` parameters along with a query. 

Let's limit our results to 2, to show this working: 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=*:*&fl=name,manu,price&rows=2"`{{execute}}

And to show _all_ results, let's increase the `rows` count to 100. 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=*:*&fl=name,manu,price&rows=100"`{{execute}}

In a real search results page, you may want 10 results per page, and a way to tell Solr that you want page 1, 2, 3 and so on. We can combine the `rows=10` parameter with an offset, `start=21`. This will return results 21-30. 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=*:*&fl=name,manu,price&rows=10&start=21"`{{execute}}

Searching for multiple terms defaults to an `OR`. So, `q=name:video ipod` is the asking Solr for matches `where name contains video OR ipod`. 

As we're using the HTTP endpoint for search, we must URL-encode a space ` ` with `%20`. 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,score&q=name:video%20ipod"`{{execute}}

```
{
  "name":["Apple 60 GB iPod with Video Playback Black"],
  "score":0.96357477
},
{
  "name":["ATI Radeon X1900 XTX 512 MB PCIE Video Card"],
  "score":0.9150753}]
}
```

We'll get into the `score` property soon - but you can think of it simply as a measure of _relevancy_ for a document against the provided search criteria. 

`OR` is great for a default search operator. But what if we wanted to search for any documents containing the exact _phrase_ `video playback`? Solr treats any search query wrapped in double-quotes as a phrase, and will only return documents containing that exact phrase. 

We must URL-encode our double-quotes with `%22`.

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,score&q=name:%22video%20playback%22"`{{execute}}

Perfect! There are a few more tools we can use here. We may want to _score_ documents highly if two _terms_ appear close together. Let's search for any documents where `video` and `black` appear next to each other in the `name` field: 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,score&q=name:%22video%20black%22"`{{execute}}

`0` results. No good. But, what if we were happy with any results where `video` and `black` appear close-by, but not necessarily next to each other? We can perform a _proximity search_, telling Solr to return any results where the terms appear within a _distance_ of 5 other terms. A proximity search uses the tilde `~` character, such as: `q=name:"video black"~5`

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,score&q=name:%22video%20black%22~5"`{{execute}}

Just like the `OR` query we ran earlier, we can use `AND` to specify two or more terms which must appear in the `name` field, with `q=name:(apple AND ipod)`

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,score&q=name:(apple%20AND%20ipod)"`{{execute}}

Lastly, Solr supports _range_ queries, which here allow us to return any products having a price between `300` and `600`. Range queries use the format: `q=price:[300 TO 600]`. We must URL-encode the `[` and `]` with `%5B` and `%5D`.

`curl "http://localhost:8983/solr/techproducts/select?indent=on&fl=name,price&q=price:%5B300%20TO%20600%5D"`{{execute}}