package main

import (
	"crypto/tls"
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	client := http.Client{Transport: &http.Transport{
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: true,
		},
	}}

	//?name=KR_DEV_MAAS_BACKEND_SYM_01
	req, err := http.NewRequest("GET", "https://cckms.hyundai.com:8444/xkm-rest/test/managedobject/symmetrickey", nil)
	if err != nil {
		log.Fatalln(req)
	}
	req.Header.Add("Authorization", "348b60347e8580ccd830dc603511bb14e59cb229")
	q := req.URL.Query()
	q.Add("name", "KR_DEV_MAAS_BACKEND_SYM_01")
	req.URL.RawQuery = q.Encode()

	log.Println(req.URL.String())

	res, err := client.Do(req)
	if err != nil {
		log.Fatalln(err)
	}
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatalln(err)
	}
	//resBody := map[string]interface{}{}

	type kmsResponse struct {
		CryptographicLength    int    `json:"cryptographicLength"`
		KeyFormatType          string `json:"keyFormatType"`
		DeactivationDate       string `json:"deactivationDate"`
		KeyMaterial            string `json:"KeyMaterial"`
		Name                   string `json:"name"`
		Digest                 string `json:"digest"`
		CryptographicAlgorithm string `json:"cryptographicAlgorithm"`
		State                  string `json:"state"`
		ActivationDate         string `json:"activationDate"`
		UniqueIdentifier       string `json:"uniqueIdentifier"`
		ObjectType             string `json:"objectType"`
	}
	type Test struct {
		Key1 int   `json:"key1"`
		Key2 int   `json:"key2,string"`
		Key3 []int `json:"key3"`
	}
	response := kmsResponse{}
	if err := json.Unmarshal(body, &response); err != nil {
		log.Fatalln(err)
	}

	log.Printf("%v", response)
	log.Println(string(body))

	testJson := []byte(`{"key1":1, "key2":"2", "key3":[1,2,3]}`)
	testStruct := &Test{}
	json.Unmarshal(testJson, testStruct)
	log.Println(testStruct)
	stubResponse := []byte(`{"cryptographicLength":256,"keyFormatType":"Raw","deactivationDate":"20330731145959","KeyMaterial":"bfc1ec170e62ef3e482e8e93cb34793b4ad2eab49833ebc8d27726c65e37d3c2","name":"KR_DEV_CCSP_ACCOUNT_SYM_01","digest":"2fec27d57f061b79a4f94d5486a83f309c3643c2e83701b96bc9bf8485a10fce","cryptographicAlgorithm":"AES","state":"Active","activationDate":"20180730150000","uniqueIdentifier":"dece100d-db03-4606-a255-4a83fd1cd781","objectType":"SymmetricKey"}`)
	log.Println(string(stubResponse))
}

//client := &http.Client{
//CheckRedirect: redirectPolicyFunc,
//}
//
//resp, err := client.Get("http://example.com")
//// ...
//
//req, err := http.NewRequest("GET", "http://example.com", nil)
//// ...
//req.Header.Add("If-None-Match", `W/"wyzzy"`)
//resp, err := client.Do(req)
//// ...
