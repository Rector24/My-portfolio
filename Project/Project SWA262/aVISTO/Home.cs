using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace aVISTO
{
    public partial class Home : Form
    {
        SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-2LP800J\SQLEXPRESS;Initial Catalog=BCExam;Integrated Security=True");

        public Home()
        {
            InitializeComponent();
        }

        private void Home_Load(object sender, EventArgs e)
        {
            

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
           


            }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.Hide();
            Login login = new Login();
            login.Show();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            this.Hide();
            Form1 form = new Form1();
            form.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
           
        }

        private void dataGridView1_CellContentClick_1(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
           
            SqlCommand cmd = new SqlCommand("SELECT id, Snum,Fname,DOB,address,gender,Phone,Modul,password FROM RegistrationTBL where Snum=@Snum",connection);
            cmd.Parameters.AddWithValue("@Snum", textBox1.Text);
            SqlDataAdapter da = new SqlDataAdapter();
            da.SelectCommand = cmd;
            DataTable table = new DataTable();
            table.Clear();
            da.Fill(table);
            dataGridView1.DataSource = table;
            dataGridView1.AllowUserToAddRows = false;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            for (int item=0; item<dataGridView1.Rows.Count-1;item++)
            {
                SqlCommand cmd2 = new SqlCommand("Update RegistraionTBL Snum=@Snum,Fname=@Fname,DOB=@DOB,address=@address,gender=@gender,Phone=@Phone,Modul=@Modul,password=@Password where id=@id",connection);
                cmd2.Parameters.AddWithValue("@Snum", dataGridView1.Rows[item].Cells[1].Value);
                cmd2.Parameters.AddWithValue("@Fname", dataGridView1.Rows[item].Cells[2].Value);
                cmd2.Parameters.AddWithValue("@DOB", Convert.ToDateTime(dataGridView1.Rows[item].Cells[3].Value));
                cmd2.Parameters.AddWithValue("@address", dataGridView1.Rows[item].Cells[4].Value);
                cmd2.Parameters.AddWithValue("@gender", dataGridView1.Rows[item].Cells[5].Value);
                cmd2.Parameters.AddWithValue("@Phone", dataGridView1.Rows[item].Cells[6].Value);
                cmd2.Parameters.AddWithValue("@Modul", dataGridView1.Rows[item].Cells[7].Value);
                cmd2.Parameters.AddWithValue("@password", dataGridView1.Rows[item].Cells[8].Value);
                cmd2.Parameters.AddWithValue("id", dataGridView1.Rows[item].Cells[0].Value);
                connection.Open();
                cmd2.ExecuteNonQuery();
                connection.Close();

            }
            MessageBox.Show("Successfull Update");
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            SqlCommand cmd3 = new SqlCommand("Delete from RegistrationTBL where id=@id",connection);
            cmd3.Parameters.AddWithValue("id", dataGridView1.CurrentRow.Cells[0].Value);
            connection.Open();
            cmd3.ExecuteNonQuery();
            connection.Close();
            MessageBox.Show("Successfull Deleted");
        }
    }
    }

