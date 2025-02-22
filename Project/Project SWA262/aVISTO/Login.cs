using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;
using System.Data.SqlClient;


namespace aVISTO
{
    public partial class Login : Form
    {
        public Login()
        {
            InitializeComponent();
        }
        SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-2LP800J\SQLEXPRESS;Initial Catalog=BCExam;Integrated Security=True");
        SqlCommand command;

        int usernameCheck(string Snum, string password)
        {
            connection.Open();
            string query = "select count(*) from RegistrationTBL where Snum='" + Snum + "' and Password='" + password + "'";
            SqlCommand command = new SqlCommand(query, connection);
            int v = (int)command.ExecuteScalar();
            connection.Close();
            return v;
        }


        private void Login_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
          
            try
            {

                if (Snum.Text!= "" && password.Text!= "")
                {
                    int v = usernameCheck(Snum.Text, password.Text);
                    if (v == 1)
                    {
                        MessageBox.Show("You have successfully entered");
                        Snum.Text = "";
                        password.Text = "";
                        this.Hide();
                        Home home = new Home();
                        home.Show();
                    }
                    else
                    {
                        MessageBox.Show("Information is not available !!!!");
                    }
                }
                else
                {
                    MessageBox.Show("Fill in the fields!!!");

                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.Hide();
            Form1 form1 = new Form1();
            form1.Show();
        }
    }

}

