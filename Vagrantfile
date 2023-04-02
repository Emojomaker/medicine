Vagrant.configure("2") do |config|
  config.vm.define "backend-1" do |backend|
  backend.vm.box = "centos/7"
  backend.vm.hostname = 'backend-1'
  backend.vm.box_url = "centos/7"
  backend.vm.network :private_network, ip: "192.168.56.5"
  end

  config.vm.define "database-1" do |database|
  database.vm.box = "centos/7"
  database.vm.hostname = 'database-1'
  database.vm.box_url = "centos/7"
  database.vm.network :private_network, ip: "192.168.56.6"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "installer/playbook.yml"
    ansible.groups = { 
      "database" => ["database-1"], 
      "backend" => ["backend-1"],
      "all_groups:children" => ["database", "backend"],
    }
    ansible.verbose = 'vv'
    ansible.vault_password_file = "/Users/a1/Documents/git/medicine/provision/pass"
  end
end