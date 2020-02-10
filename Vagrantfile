#agr -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  #config.vm.box_version = "1.8.14"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8081, host: 8081

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false

    # Customize the amount of memory on the VM:
    vb.memory = "4096"
    vb.cpus = "2"

    # Custom Name for the VM
    vb.name = "CoinBase Developer VM"

    # Adding DNS resolver
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]

    # Set the NIC for security reasons
    vb.default_nic_type = "AM79C973"

  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  #turn on x11 forwarding
  config.ssh.forward_x11 = true
  config.ssh.forward_agent = true

  #map shared folder
  config.vm.synced_folder ENV['HOME'], '/home/vagrant/host'
  config.vm.synced_folder ".", "/vagrant", disabled: true
  # Prefer VMware Fusion before VirtualBox
  config.vm.provider "virtualbox"

  # Upgrade the VM
  config.vm.provision "shell", inline: <<-UPGRADE
    export DEBIAN_FRONTEND=noninteractive
    apt-get update -qq
    apt-get -y -qq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
  UPGRADE

  # Install development tools
  config.vm.provision "shell", inline: <<-DEVTOOLS
    # Making X Forwarding work with SSH
    sed -i 's/^#AddressFamily any$/AddressFamily inet/' /etc/ssh/sshd_config
    service ssh restart

   # Install Python and modules
   apt install -y python python-pip
   pip install lendingclub
  DEVTOOLS

  # Reboot the VM and wait for reconnection
  config.vm.provision :reload

end
