terraform {
  cloud {
    organization = "budkee"

    workspaces {
      name = "tads_api"
    }
  }
}