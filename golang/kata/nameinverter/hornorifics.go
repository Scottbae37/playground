package nameinverter

func IsHonorific(s string) bool {
	if s == "Mr." {
		return true
	}
	if s == "Mrs." {
		return true
	}
	return false
}
